package lanminecraft.desolate.hqm.mixin;

import hardcorequesting.common.forge.client.interfaces.graphic.QuestSetsGraphic;
import hardcorequesting.common.forge.quests.QuestSet;
import lanminecraft.desolate.hqm.LocalizedHqmText;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Redirect;

@Mixin(value = QuestSetsGraphic.class, remap = false)
abstract class QuestSetsGraphicMixin {
    // Use the same title for rendering and click hitboxes, including the chapter number.
    @Redirect(method = {"draw(Lnet/minecraft/client/gui/GuiGraphics;II)V", "onClick(III)V"},
        at = @At(value = "INVOKE",
            target = "Lhardcorequesting/common/forge/quests/QuestSet;getName(I)Ljava/lang/String;", remap = false),
        require = 2)
    private String desolateHqm$chapterLabel(QuestSet chapter, int index) {
        return (index + 1) + ". " + LocalizedHqmText.chapter(chapter.getName());
    }
}
