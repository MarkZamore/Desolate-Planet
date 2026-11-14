    private void verifyRespawn() throws Exception {
        Object server = onClient(this::server);
        UUID playerId = onClient(() -> (UUID) invoke(player(), "m_20148_"));
        boolean keep = !reopenLevelSha256.isEmpty();
        String marker = keep ? "keep-inventory" : "corpse";
        Object deadPlayer = schedule((Executor) server, () -> {
            Object worldData = invoke(server, "m_129910_");
            require(Boolean.FALSE.equals(invoke(worldData, "m_5466_")), "The world is Hardcore.");
            require("SURVIVAL".equals(((Enum<?>) invoke(worldData, "m_5464_")).name()), "The world is not Survival.");
            require("NORMAL".equals(((Enum<?>) invoke(worldData, "m_5472_")).name()), "The world is not Normal difficulty.");
            require(keep == readWorldRule(server, "f_46133_"), "Unexpected saved keepInventory.");
            require(!readWorldRule(server, "f_46124_"), "Author default doPatrolSpawning was not retained.");
            Object host = serverPlayer(server, playerId);
            require(countInPlayer(host, marker) == 0, "The marker already exists.");
            Object stackTypeItem = type("net.minecraft.resources.ResourceLocation").getConstructor(String.class)
                .newInstance("minecraft:carrot");
            Object items = type("net.minecraft.core.registries.BuiltInRegistries").getField("f_257033_").get(null);
            Object item = invoke(items, "m_7745_", new Class<?>[] {stackTypeItem.getClass()}, stackTypeItem);
            Class<?> stackType = type("net.minecraft.world.item.ItemStack");
            Object stack = stackType.getConstructor(type("net.minecraft.world.level.ItemLike"), int.class)
                .newInstance(item, 3);
            Object tag = invoke(type("net.minecraft.nbt.StringTag"), null, "m_129297_",
                new Class<?>[] {String.class}, marker);
            invoke(stack, "m_41700_", new Class<?>[] {String.class, type("net.minecraft.nbt.Tag")}, "LanMcRespawnQa", tag);
            require(Boolean.TRUE.equals(invoke(invoke(host, "m_150109_"), "m_36054_",
                new Class<?>[] {stackType}, stack)), "Could not give the test marker.");
            require(countInPlayer(host, marker) == 3, "Unexpected inventory marker count before death.");
            invoke(host, "m_6074_");
            return host;
        });
        waitUntil("active vanilla Respawn button", 120, () -> onClient(() -> {
            Object screen = screen();
            if (!type(SCREENS + "DeathScreen").isInstance(screen)) return false;
            List<Object> actions = visibleActions(screen, "deathScreen.respawn");
            if (actions.size() != 1 || !isActive(actions.get(0))) return false;
            activateNativeAction(screen, "deathScreen.respawn");
            return true;
        }));
        waitUntil("respawn in Survival", 150, () -> {
            boolean revived = schedule((Executor) server, () -> {
                Object current = serverPlayer(server, playerId);
                return current != null && current != deadPlayer
                    && Boolean.TRUE.equals(invoke(current, "m_6084_"))
                    && Boolean.FALSE.equals(invoke(current, "m_5833_"));
            });
            return revived && onClient(() -> screen() == null);
        });
        Map<String, Object> checks = schedule((Executor) server, () -> {
            Object host = serverPlayer(server, playerId);
            Object level = invoke(host, "m_284548_");
            Object markedCorpse = null;
            int corpseCount = 0;
            for (Object corpse : corpses(level)) {
                if (!((Optional<?>) invoke(corpse, "getCorpseUUID")).filter(playerId::equals).isPresent()) continue;
                int items = corpseMarkerCount(corpse, marker);
                corpseCount += items;
                if (items > 0) markedCorpse = corpse;
            }
            int before = countInPlayer(host, marker);
            if (keep) {
                require(before == 3 && corpseCount == 0, "keepInventory lost or duplicated the marker stack.");
            } else {
                require(before == 0 && corpseCount == 3 && markedCorpse != null, "Death did not transfer all markers to the corpse.");
                Class<?> hand = type("net.minecraft.world.InteractionHand");
                invoke(markedCorpse, "m_6096_", new Class<?>[] {type("net.minecraft.world.entity.player.Player"), hand},
                    host, hand.getField("MAIN_HAND").get(null));
                Object container = field(host.getClass(), "f_36096_").get(host);
                require(type("de.maxhenkel.corpse.gui.CorpseInventoryContainer").isInstance(container),
                    "The player's corpse did not open the native inventory.");
                invoke(container, "transferItems");
                require(countInPlayer(host, marker) == 3 && corpseMarkerCount(markedCorpse, marker) == 0,
                    "Native Corpse transfer lost or duplicated the marker stack.");
                invoke(host, "m_6915_");
                Object rule = invoke(invoke(invoke(server, "m_129910_"), "m_5470_"), "m_46170_",
                    new Class<?>[] {type(LEVEL + "GameRules$Key")}, keepInventoryKey());
                invoke(rule, "m_46246_", new Class<?>[] {boolean.class, type("net.minecraft.server.MinecraftServer")}, true, server);
                require(readWorldRule(server, "f_46133_"), "The server did not save the keepInventory change.");
            }
            return Map.of("keepInventoryAtDeath", keep, "itemsInCorpse", corpseCount, "itemsAtRespawn", before,
                "itemsAfterRecovery", countInPlayer(host, marker), "survivalRespawn", true,
                "nativeCorpseTransfer", !keep, "keepInventoryForNextLoad", readWorldRule(server, "f_46133_"),
                "doPatrolSpawning", readWorldRule(server, "f_46124_"));
        });
        event("respawn_and_inventory", checks);
    }

    private Object serverPlayer(Object server, UUID id) throws ReflectiveOperationException {
        return invoke(invoke(server, "m_6846_"), "m_11259_", new Class<?>[] {UUID.class}, id);
    }

    private Object keepInventoryKey() throws ReflectiveOperationException {
        return type(LEVEL + "GameRules").getField("f_46133_").get(null);
    }

    private boolean readWorldRule(Object server, String keyName) throws ReflectiveOperationException {
        Object rules = invoke(invoke(server, "m_129910_"), "m_5470_");
        Object rule = type(LEVEL + "GameRules").getField(keyName).get(null);
        return Boolean.TRUE.equals(invoke(rules, "m_46207_", new Class<?>[] {type(LEVEL + "GameRules$Key")}, rule));
    }

    private List<?> corpses(Object level) throws ReflectiveOperationException {
        Class<?> entityTypeTest = type(LEVEL + "entity.EntityTypeTest");
        Object test = invoke(entityTypeTest, null, "m_156916_", new Class<?>[] {Class.class},
            type("de.maxhenkel.corpse.entities.CorpseEntity"));
        java.util.function.Predicate<Object> all = ignored -> true;
        return (List<?>) invoke(level, "m_143280_", new Class<?>[] {entityTypeTest, java.util.function.Predicate.class}, test, all);
    }

    private int corpseMarkerCount(Object corpse, String marker) throws ReflectiveOperationException {
        return countMarker((List<?>) invoke(invoke(corpse, "getDeath"), "getAllItems"), marker);
    }

    private int countInPlayer(Object player, String marker) throws ReflectiveOperationException {
        Object inventory = invoke(player, "m_150109_");
        return countMarker((List<?>) field(inventory.getClass(), "f_35974_").get(inventory), marker);
    }

    private int countMarker(List<?> stacks, String marker) throws ReflectiveOperationException {
        int count = 0;
        for (Object stack : stacks) {
            Object tag = invoke(stack, "m_41783_");
            if (tag != null && marker.equals(invoke(tag, "m_128461_", new Class<?>[] {String.class}, "LanMcRespawnQa"))) {
                count += (Integer) invoke(stack, "m_41613_");
            }
        }
        return count;
    }
