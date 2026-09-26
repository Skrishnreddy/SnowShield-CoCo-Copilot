import os
import subprocess
from PIL import Image

ffmpeg_exe = "/Users/gsaikrishnareddy/pandashield-v2/venv/lib/python3.14/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1"
work_dir = "/Users/gsaikrishnareddy/pandashield-v2/Snowflake"
audio_dir = os.path.join(work_dir, "audio_scenes")
tmp_dir = os.path.join(work_dir, "video_tmp")
os.makedirs(tmp_dir, exist_ok=True)

TARGET_W, TARGET_H = 1280, 720

def prepare_image(src_path, dst_path):
    img = Image.open(src_path).convert("RGB")
    img.thumbnail((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (TARGET_W, TARGET_H), (15, 23, 42)) # Slate 900 background
    offset_x = (TARGET_W - img.width) // 2
    offset_y = (TARGET_H - img.height) // 2
    canvas.paste(img, (offset_x, offset_y))
    canvas.save(dst_path, "PNG")

# Image sources
images = {
    "slide1": os.path.join(work_dir, "final_slide_1.png"),
    "slide3": os.path.join(work_dir, "final_slide_3.png"),
    "slide4": os.path.join(work_dir, "final_slide_4.png"),
    "slide5": os.path.join(work_dir, "final_slide_5.png"),
    "slide6": os.path.join(work_dir, "final_slide_6.png"),
    "tab1": "/Users/gsaikrishnareddy/.gemini/antigravity-ide/brain/23558058-8d05-4f65-a21b-4b467e919bce/tab1_telemetry_1790434094441.png",
    "tab1_res": "/Users/gsaikrishnareddy/.gemini/antigravity-ide/brain/23558058-8d05-4f65-a21b-4b467e919bce/tab1_cortex_result_1790434154739.png",
    "tab2": "/Users/gsaikrishnareddy/.gemini/antigravity-ide/brain/23558058-8d05-4f65-a21b-4b467e919bce/tab2_compliance_1790434223159.png",
    "tab3": "/Users/gsaikrishnareddy/.gemini/antigravity-ide/brain/23558058-8d05-4f65-a21b-4b467e919bce/tab3_autofix_1790434298037.png",
    "tab4": "/Users/gsaikrishnareddy/.gemini/antigravity-ide/brain/23558058-8d05-4f65-a21b-4b467e919bce/tab4_chat_1790434451006.png",
}

for k, p in images.items():
    dst = os.path.join(tmp_dir, f"{k}_1280.png")
    prepare_image(p, dst)
print("All 1280x720 frames prepared.")

scenes = [
    ("scene1_title", [("slide1", 10.13)]),
    ("scene2_problem", [("slide3", 14.30)]),
    ("scene3_arch", [("slide4", 12.22)]),
    ("scene4_telemetry", [("tab1", 5.5), ("tab1_res", 7.34)]),
    ("scene5_compliance", [("tab2", 4.5), ("tab3", 4.5), ("tab4", 5.01)]),
    ("scene6_impact", [("slide5", 11.5), ("slide6", 5.93)]),
]

scene_mp4s = []
for idx, (scene_name, frame_list) in enumerate(scenes):
    audio_wav = os.path.join(audio_dir, f"{scene_name}.wav")
    scene_mp4 = os.path.join(tmp_dir, f"{scene_name}.mp4")
    
    if len(frame_list) == 1:
        img_file = os.path.join(tmp_dir, f"{frame_list[0][0]}_1280.png")
        cmd = [
            ffmpeg_exe, "-y",
            "-loop", "1", "-i", img_file,
            "-i", audio_wav,
            "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p", "-shortest",
            scene_mp4
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        concat_txt = os.path.join(tmp_dir, f"{scene_name}_frames.txt")
        with open(concat_txt, "w") as f:
            for img_key, dur in frame_list:
                img_path = os.path.join(tmp_dir, f"{img_key}_1280.png")
                f.write(f"file '{img_path}'\n")
                f.write(f"duration {dur}\n")
            f.write(f"file '{img_path}'\n")
            
        cmd = [
            ffmpeg_exe, "-y",
            "-f", "concat", "-safe", "0", "-i", concat_txt,
            "-i", audio_wav,
            "-c:v", "libx264", "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p", "-shortest",
            scene_mp4
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    scene_mp4s.append(scene_mp4)
    print(f"Generated scene clip: {scene_mp4}")

final_concat_txt = os.path.join(tmp_dir, "final_scenes.txt")
with open(final_concat_txt, "w") as f:
    for s_mp4 in scene_mp4s:
        f.write(f"file '{s_mp4}'\n")

final_mp4 = os.path.join(work_dir, "SnowShield_Demo_Video.mp4")
cmd_merge = [
    ffmpeg_exe, "-y",
    "-f", "concat", "-safe", "0", "-i", final_concat_txt,
    "-c", "copy",
    final_mp4
]
subprocess.run(cmd_merge, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("SUCCESS: Merged into final video:", final_mp4)
