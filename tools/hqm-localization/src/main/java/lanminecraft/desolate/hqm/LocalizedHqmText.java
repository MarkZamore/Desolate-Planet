package lanminecraft.desolate.hqm;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HexFormat;
import java.util.Map;
import net.minecraft.locale.Language;

public final class LocalizedHqmText {
    private static final String INTRO_KEY = "desolate_hqm_localization.mat_report";
    private static final String AUTHOR_INTRO_SHA256 = "6536e1a4278d4ea638861ea02eaeb9617b1190585b4403cbe0498b44bbcc1b4f";
    private static final Map<String, String> CHAPTER_KEYS = Map.of(
        "Basic Survival", "hqm.quest_set.basic_survival.name",
        "The Food Pyramid", "hqm.quest_set.the_food_pyramid.name",
        "Like Clockwork", "hqm.quest_set.like_clockwork.name",
        "Under Pressure", "hqm.quest_set.under_pressure.name",
        "Salvage Operation", "hqm.quest_set.salvage_operation.name",
        "Technological Revolution", "hqm.quest_set.technological_revolution.name",
        "To Infinity and Beyond", "hqm.quest_set.to_infinity_and_beyond.name"
    );

    private LocalizedHqmText() {
    }

    public static String chapter(String original) {
        if (original == null) return null;
        String key = CHAPTER_KEYS.get(original);
        return key == null ? original : Language.m_128107_().m_118919_(key, original);
    }

    public static String intro(String original) {
        if (original == null) return null;
        String translated = Language.m_128107_().m_118919_(INTRO_KEY, original);
        if (translated.equals(original)) return original;

        // Do not replace an introduction edited by the host or from a different quest pack.
        String normalized = original.replace("\r\n", "\n").stripTrailing();
        return AUTHOR_INTRO_SHA256.equals(sha256(normalized)) ? translated : original;
    }

    private static String sha256(String value) {
        try {
            byte[] hash = MessageDigest.getInstance("SHA-256").digest(value.getBytes(StandardCharsets.UTF_8));
            return HexFormat.of().formatHex(hash);
        } catch (NoSuchAlgorithmException e) {
            throw new AssertionError(e);
        }
    }
}
