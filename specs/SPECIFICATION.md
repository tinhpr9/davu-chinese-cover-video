# Specification: Dạ Vũ (夜舞) - Chinese Version Viral TikTok Video

## 1. Overview
- **Project**: Chinese version cover video of Vietnamese hit "Dạ Vũ" (Tăng Duy Tân).
- **Vocal**: Professional studio recording by Chinese artist Hoàng Linh (黄龄).
- **Format**: Vertical short-form video (1080x1920, 9:16), 30 FPS.
- **Target Platform**: TikTok / Douyin / Reels / Shorts.
- **Duration**: ~56 seconds (from 00:32.0 to 01:28.0 of the song, covering the verse buildup, pre-chorus, and iconic Guzheng/flute drop).

## 2. Audio Architecture
- **Source**: `assets/davu_chinese_original.mp3`
- **Output**: `output/davu_chorus_56s.mp3`
- **Processing**:
  - Start: 32.0s
  - Duration: 56.0s
  - Fade-in: 0.5s audio smooth curve
  - Fade-out: 1.5s audio smooth curve
  - Sample rate: 44100 Hz, Stereo, 192kbps

## 3. Subtitle Architecture (3-Layer TikTok Viral Standard)
- Format: Advanced SubStation Alpha (`.ass`)
- Resolution: PlayResX=1080, PlayResY=1920
- Alignment: Center-Bottom (`Alignment=2`)
- Layers:
  1. **Layer 1 (Hán tự)**: Font size ~52pt, Bold, White text (`#FFFFFF`) with dark subtle glow/outline (`#1A102F`), MarginV ~420.
  2. **Layer 2 (Pinyin with Tones)**: Font size ~30pt, Italic/Light, Warm Gold (`#FFD166`), MarginV ~360.
  3. **Layer 3 (Việt sub)**: Font size ~34pt, Semi-bold, Soft Cyan/White (`#E0F7FA`), MarginV ~300.
- Timings:
  - 00:03.0 -> 00:10.0: `树影灯影底随月影在摇晃` / `Shù yǐng dēngyǐng dǐ suí yuèyǐng zài yáohuàng` / `Bóng cây ánh đèn cùng đung đưa theo ánh trăng`
  - 00:10.0 -> 00:18.0: `慌的心中所想无处去隐藏` / `Huāng de xīnzhōng suǒ xiǎng wú chù qù yǐncáng` / `Những ý nghĩ hốt hoảng trong lòng không thể giấu kín`
  - 00:18.0 -> 00:26.0: `勾勒出被遗忘的念念不忘` / `Gōulè chū bèi yíwàng de niànniànbùwàng` / `Phác họa ra những nỗi nhớ mãi mãi không quên`
  - 00:26.0 -> 00:34.0: `冰凉的是否还能变滚烫` / `Bīngliáng de shìfǒu hái néng biàn gǔntàng` / `Lạnh lẽo phải chăng có thể trở nên nóng bỏng`
  - 00:34.0 -> 00:42.0: `谁翻云覆雨冷不防` / `Shéi fānyúnfùyǔ lěngbùfáng` / `Là ai bất chợt gió mưa thất thường`
  - 00:42.0 -> 00:56.0: `随风起舞 叹这长夜` / `Suí fēng qǐ wǔ, tàn zhè cháng yè` / `Nhảy múa cùng làn gió, than thở khúc đêm dài ♫ [DROP BEAT]`

## 4. Visual Architecture
- **Base Canvas**: Vertical 1080x1920 artwork (`assets/background_base.jpg`).
- **Motion Effects**:
  - Ken Burns slow push-in / gentle breathing zoom (`zoompan`).
  - Overlay header: Song title badge `DẠ VŨ (夜舞) | CHINESE COVER` & Singer `Hoàng Linh (黄龄)`.
  - Vinyl record / visualizer accent pulse during the drop.
  - Subtitle burn-in via libass filter.

## 5. Verification & Deployment
- Automated tests covering audio duration, subtitle syntax, video resolution, FPS, and audio-video sync.
- ADB transfer to target device: `/storage/emulated/0/DCIM/Camera/` & `/storage/emulated/0/Movies/`.
