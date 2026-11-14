package lanminecraft.desolate.hqm.mixin;

import hardcorequesting.common.forge.client.interfaces.graphic.MainPageGraphic;
import hardcorequesting.common.forge.util.Translator;
import java.util.List;
import lanminecraft.desolate.hqm.LocalizedHqmText;
import net.minecraft.locale.Language;
import net.minecraft.network.chat.FormattedText;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.Unique;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.Redirect;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

@Mixin(value = MainPageGraphic.class, remap = false)
abstract class MainPageGraphicMixin {
    @Shadow private List<FormattedText> cachedMainDescription;
    @Unique private Language desolateHqm$descriptionLanguage;

    @Inject(method = "getDescriptionLines", at = @At("HEAD"), require = 1)
    private void desolateHqm$refreshOnLanguageChange(CallbackInfoReturnable<List<FormattedText>> callback) {
        Language language = Language.m_128107_();
        if (language != desolateHqm$descriptionLanguage) {
            desolateHqm$descriptionLanguage = language;
            cachedMainDescription = null;
        }
    }

    @Redirect(method = "getDescriptionLines", at = @At(value = "INVOKE",
        target = "Lhardcorequesting/common/forge/util/Translator;plain(Ljava/lang/String;)Lnet/minecraft/network/chat/FormattedText;",
        remap = false), require = 1)
    private FormattedText desolateHqm$localizedIntro(String original) {
        return Translator.plain(LocalizedHqmText.intro(original));
    }
}
