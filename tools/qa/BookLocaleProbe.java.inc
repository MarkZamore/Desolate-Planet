    private void verifyBookLocales() throws Exception {
        // Reload only the language and the two client guide registries. A complete
        // texture/model reload would test unrelated resources and dominate this check.
        Map<String, Object> checks = onClient(() -> {
            Object manager = invoke(client, "m_91102_");
            String original = (String) invoke(manager, "m_264236_");
            Object resources = invoke(client, "m_91098_");
            Class<?> resourceManager = type("net.minecraft.server.packs.resources.ResourceManager");
            Class<?> patchouliRegistry = type("vazkii.patchouli.client.book.ClientBookRegistry");
            Object patchouli = patchouliRegistry.getField("INSTANCE").get(null);
            Class<?> questBook = type("hardcorequesting.common.forge.client.interfaces.GuiQuestBook");
            var bookConstructor = questBook.getDeclaredConstructor(type("net.minecraft.world.entity.player.Player"), boolean.class);
            bookConstructor.setAccessible(true);
            Object book = bookConstructor.newInstance(player(), false);
            field(questBook, "f_96547_").set(book, field(client.getClass(), "f_91062_").get(client));
            String graphics = "hardcorequesting.common.forge.client.interfaces.graphic.";
            Object frontPage = type(graphics + "MainPageGraphic").getConstructor(questBook).newInstance(book);
            Class<?> setsPage = type("hardcorequesting.common.forge.client.BookPage$SetsPage");
            Object chapters = type(graphics + "QuestSetsGraphic").getConstructor(setsPage, questBook)
                .newInstance(setsPage.getField("INSTANCE").get(null), book);
            var results = new LinkedHashMap<String, Object>();
            try {
                for (String locale : List.of("en_us", "ru_ru", "en_us")) {
                    reloadBookLanguage(manager, resourceManager, resources, patchouli, locale);
                    Map<String, Object> sample = readBookSamples(locale, resources);
                    sample.putAll(readHqmFrontPage(locale, frontPage, chapters));
                    Object previous = results.put(locale, sample);
                    require(previous == null || previous.equals(sample), "Book locale results changed when returning to English.");
                }
            } finally {
                reloadBookLanguage(manager, resourceManager, resources, patchouli, original);
            }
            return results;
        });
        event("native_book_locales", checks);
    }

    private void reloadBookLanguage(Object manager, Class<?> resourceManager, Object resources,
                                    Object patchouli, String locale) throws Exception {
        invoke(manager, "m_264110_", new Class<?>[] {String.class}, locale);
        invoke(manager, "m_6213_", new Class<?>[] {resourceManager}, resources);
        invoke(patchouli, "reload");

        Class<?> guideReload = type("guideme.internal.GuideReloadListener");
        var constructor = guideReload.getDeclaredConstructor();
        constructor.setAccessible(true);
        Object reloader = constructor.newInstance();
        Class<?> profilerType = type("net.minecraft.util.profiling.ProfilerFiller");
        Object profiler = type("net.minecraft.util.profiling.InactiveProfiler").getField("f_18554_").get(null);
        Object result = invoke(reloader, "prepare", new Class<?>[] {resourceManager, profilerType},
            resources, profiler);
        invoke(reloader, "apply", new Class<?>[] {result.getClass(), resourceManager, profilerType},
            result, resources, profiler);
    }

    private Map<String, Object> readBookSamples(String locale, Object resources) throws Exception {
        boolean russian = locale.equals("ru_ru");
        Class<?> resourceLocation = type("net.minecraft.resources.ResourceLocation");
        var actual = new LinkedHashMap<String, Object>();
        actual.put("buildingGadgets", expectBookText("Building Gadgets",
            patchouliEntryName("buildinggadgets2:buildinggadgets2book", "buildinggadgets2:basics"),
            russian ? "Основы" : "Basics"));
        actual.put("industrialForegoing", expectBookText("Industrial Foregoing",
            patchouliEntryName("industrialforegoing:industrial_foregoing",
                "industrialforegoing:resource_production/fluid_collector"),
            russian ? "Жидкостный собиратель" : "Fluid Collector"));
        actual.put("pneumaticCraft", expectBookText("PneumaticCraft",
            patchouliEntryName("pneumaticcraft:book", "pneumaticcraft:base_concepts/oil"),
            russian ? "Сырая нефть" : "Crude Oil"));

        Class<?> mantle = type("slimeknights.mantle.client.book.repository.FileRepository");
        Object repository = mantle.getConstructor(resourceLocation).newInstance(
            bookLocation("tconstruct:book/materials_and_you"));
        Object page = invoke(repository, "getResourceLocation", new Class<?>[] {String.class, boolean.class},
            "tools/recycling.json", false);
        String expectedPath = "tconstruct:book/materials_and_you/" + locale + "/tools/recycling.json";
        require(page != null && expectedPath.equals(page.toString()), "Mantle did not select " + expectedPath);
        Optional<?> resource = (Optional<?>) invoke(resources, "m_213713_", new Class<?>[] {resourceLocation}, page);
        require(resource.isPresent(), "Missing Tinkers' Construct page: " + expectedPath);
        try (var reader = (java.io.Reader) invoke(resource.get(), "m_215508_")) {
            Class<?> gsonParser = type("com.google.gson.JsonParser");
            Object json = invoke(gsonParser, null, "parseReader", new Class<?>[] {java.io.Reader.class}, reader);
            Object title = invoke(invoke(json, "getAsJsonObject"), "get", new Class<?>[] {String.class}, "title");
            actual.put("materialsAndYou", expectBookText("Materials and You",
                (String) invoke(title, "getAsString"), russian ? "Разборка инструментов" : "Recycling Tools"));
        }

        Object guide = invoke(type("guideme.internal.GuideRegistry"), null, "getById",
            new Class<?>[] {resourceLocation}, bookLocation("ae2:guide"));
        require(guide != null, "AE2 registered no GuideME guide.");
        Object index = invoke(guide, "getParsedPage", new Class<?>[] {resourceLocation}, bookLocation("ae2:index.md"));
        require(index != null, "AE2 GuideME index was missing.");
        expectBookText("AE2 index locale", (String) invoke(index, "getLanguage"), locale);
        require(invoke(guide, "getPage", new Class<?>[] {resourceLocation}, bookLocation("ae2:index.md")) != null,
            "AE2 GuideME index could not be compiled.");
        actual.put("appliedEnergisticsGuide", locale);
        int pages = 0;
        var addOnPages = new LinkedHashMap<String, Object>();
        for (Object parsed : (java.util.Collection<?>) invoke(guide, "getPages")) {
            Object id = invoke(parsed, "getId");
            String language = (String) invoke(parsed, "getLanguage");
            if (id.toString().startsWith("ae2:")) {
                expectBookText("AE2 page " + id, language, locale);
                pages++;
            } else {
                addOnPages.put(id.toString(), language);
            }
            require(invoke(guide, "getPage", new Class<?>[] {resourceLocation}, id) != null,
                "AE2 GuideME could not compile " + id);
        }
        require(pages == 119, "Unexpected AE2 guide page count: " + pages);
        actual.put("compiledAe2Pages", pages);
        actual.put("guideAddOnPages", addOnPages);

        Class<?> hqm = type("hardcorequesting.common.forge.quests.QuestSetsManager");
        Object questManager = invoke(hqm, null, "getInstance", new Class<?>[0]);
        Map<?, ?> quests = (Map<?, ?>) hqm.getField("quests").get(questManager);
        Object quest = quests.get(UUID.fromString("feb164b4-e0bf-48e0-aaec-b8bb1118c3b8"));
        require(quest != null, "HQM did not load the Gathering Supplies quest.");
        actual.put("hqmGatheringSupplies", expectBookText("HQM",
            (String) invoke(invoke(quest, "getName"), "getString"),
            russian ? "Сбор припасов" : "Gathering Supplies"));
        return actual;
    }

    private Object bookLocation(String id) throws ReflectiveOperationException {
        return type("net.minecraft.resources.ResourceLocation").getConstructor(String.class).newInstance(id);
    }

    private Map<String, Object> readHqmFrontPage(String locale, Object frontPage, Object chapters) throws Exception {
        var lines = new StringJoiner(" ");
        for (Object line : (List<?>) invoke(frontPage, "getDescriptionLines")) {
            lines.add((String) invoke(line, "getString"));
        }
        String visible = lines.toString();
        boolean russian = locale.equals("ru_ru");
        String header = russian ? "ОТЧЁТ ТЕРМИНАЛА MAT" : "MAT STATUS REPORT";
        require(visible.contains(header) && visible.contains("4en3SpWtJg") && visible.contains("Iskandar"),
            "HQM did not wrap the whole " + locale + " MAT report.");
        Class<?> questType = type("hardcorequesting.common.forge.quests.Quest");
        String original = (String) invoke(questType, null, "getRawMainDescription", new Class<?>[0]);
        require(original.contains("MAT STATUS REPORT") && !original.contains("ОТЧЁТ"),
            "HQM changed the stored English MAT report.");

        Class<?> setsManager = type("hardcorequesting.common.forge.quests.QuestSetsManager");
        Object manager = invoke(setsManager, null, "getInstance", new Class<?>[0]);
        List<?> sets = (List<?>) setsManager.getField("questSets").get(manager);
        List<String> saved = List.of("Basic Survival", "The Food Pyramid", "Like Clockwork", "Under Pressure",
            "Salvage Operation", "Technological Revolution", "To Infinity and Beyond");
        List<String> displayed = russian ? List.of("Основы выживания", "Пищевая пирамида", "Как часы", "Под давлением",
            "Поиски в руинах", "Технологическая революция", "К бесконечности и дальше") : saved;
        require(sets.size() == saved.size(), "Unexpected chapter count in the real HQM quest book.");
        var chapterLabel = java.util.Arrays.stream(chapters.getClass().getDeclaredMethods())
            .filter(method -> method.getName().endsWith("desolateHqm$chapterLabel"))
            .findFirst().orElseThrow(() -> new IllegalStateException("HQM chapter renderer mixin did not apply."));
        chapterLabel.setAccessible(true);
        var titles = new ArrayList<String>();
        for (int index = 0; index < sets.size(); index++) {
            Object set = sets.get(index);
            expectBookText("Saved HQM title", (String) invoke(set, "getName"), saved.get(index));
            String expected = (index + 1) + ". " + displayed.get(index);
            titles.add(expectBookText("Rendered HQM title", (String) chapterLabel.invoke(chapters, set, index), expected));
        }
        return Map.of("hqmMatReport", header, "hqmChapters", titles, "hqmSavedTitles", saved);
    }

    private String patchouliEntryName(String bookId, String entryId) throws Exception {
        Class<?> registryType = type("vazkii.patchouli.common.book.BookRegistry");
        Object registry = registryType.getField("INSTANCE").get(null);
        Map<?, ?> books = (Map<?, ?>) registryType.getField("books").get(registry);
        Object book = books.get(bookLocation(bookId));
        require(book != null, "Patchouli could not find " + bookId);
        Object contents = invoke(book, "getContents");
        require(Boolean.FALSE.equals(invoke(contents, "isErrored")), "Patchouli failed to load " + bookId);
        Map<?, ?> entries = (Map<?, ?>) contents.getClass().getField("entries").get(contents);
        Object entry = entries.get(bookLocation(entryId));
        require(entry != null, "Patchouli did not load " + entryId);
        return (String) invoke(invoke(entry, "getName"), "getString");
    }

    private static String expectBookText(String book, String actual, String expected) {
        require(expected.equals(actual), book + " returned " + actual + ", expected " + expected);
        return actual;
    }
