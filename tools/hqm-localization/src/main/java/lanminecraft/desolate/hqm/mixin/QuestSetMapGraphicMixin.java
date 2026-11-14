package lanminecraft.desolate.hqm.mixin;

import hardcorequesting.common.forge.client.interfaces.graphic.QuestSetMapGraphic;
import hardcorequesting.common.forge.quests.QuestSet;
import lanminecraft.desolate.hqm.LocalizedHqmText;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Redirect;

@Mixin(value = QuestSetMapGraphic.class, remap = false)
abstract class QuestSetMapGraphicMixin {
    @Redirect(method = {"addExternalParentTooltip", "addOptionLinkTooltip", "addChildTooltip"},
        at = @At(value = "INVOKE",
            target = "Lhardcorequesting/common/forge/quests/QuestSet;getName()Ljava/lang/String;", remap = false),
        require = 3)
    private String desolateHqm$tooltipChapter(QuestSet chapter) {
        return LocalizedHqmText.chapter(chapter.getName());
    }
}
