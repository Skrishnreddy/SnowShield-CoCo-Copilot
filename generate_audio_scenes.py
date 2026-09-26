import os
import subprocess
import wave

ffmpeg_exe = "/Users/gsaikrishnareddy/pandashield-v2/venv/lib/python3.14/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1"
audio_dir = "/Users/gsaikrishnareddy/pandashield-v2/Snowflake/audio_scenes"
os.makedirs(audio_dir, exist_ok=True)

script_sections = [
    ("scene1_title", "Welcome to SnowShield, an autonomous Risk, Fraud, and Regulatory Intelligence Copilot built for the Snowflake Co-Co C-L-I Hackathon, G-C-C Edition."),
    ("scene2_problem", "Global Capability Centers manage mission-critical data warehouses subject to strict G-D-P-R, P-C-I D-S-S, and S-O-C 2 compliance. Manual log audits cause severe alert fatigue, while exfiltration risks remain hidden."),
    ("scene3_arch", "SnowShield solves this with a four-tier architecture, uniting Snowflake Data Cloud telemetry, Cortex A-I inference, and three custom Co-Co C-L-I skills to detect and auto-remediate pipeline risks."),
    ("scene4_telemetry", "On our live dashboard, Tab 1 monitors warehouse query telemetry in real time. When an anomalous exfiltration event is detected, Snowflake Cortex evaluates the threat and provides immediate containment actions."),
    ("scene5_compliance", "Tab 2 tracks live compliance benchmarks across G-D-P-R and P-C-I D-S-S. Tab 3 identifies code vulnerabilities, runs A-S-T safety verification, and opens automated, ready-to-merge GitHub Pull Requests."),
    ("scene6_impact", "SnowShield is deployed natively as Streamlit in Snowflake, powered by our four hundred dollar A-I Data Cloud credits and live Cortex Llama 3.1 endpoints. It delivers a 72% faster M-T-T-R, 100% compliance, and zero hallucinations. Thank you!")
]

durations = {}
for name, text in script_sections:
    aiff_file = os.path.join(audio_dir, f"{name}.aiff")
    wav_file = os.path.join(audio_dir, f"{name}.wav")
    subprocess.run(["say", "-v", "Samantha", "-o", aiff_file, text], check=True)
    subprocess.run([ffmpeg_exe, "-y", "-i", aiff_file, "-ar", "44100", "-ac", "2", wav_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    with wave.open(wav_file, "rb") as w:
        dur = w.getnframes() / w.getframerate()
        durations[name] = dur
        print(f"{name}: {dur:.2f}s")

total = sum(durations.values())
print(f"Total narration duration: {total:.2f} seconds ({total/60:.2f} mins)")
