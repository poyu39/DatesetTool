import os
import wave
import argparse


def get_audio_length(file_path):
    with wave.open(file_path, 'rb') as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, help='包含音訊檔案的來源資料夾路徑。')
    args = parser.parse_args()
    
    audio_avg_length = 0
    audio_count = 0
    for root, _, files in os.walk(args.source):
        for file in files:
            if str(file).endswith('.wav'):
                file_path = os.path.join(root, file)
                audio_length = get_audio_length(file_path)
                audio_avg_length += audio_length
                audio_count += 1
                print(f"{file_path} 的長度為 {audio_length} 秒。")
    
    audio_avg_length /= audio_count

    with open('info.md', 'w', encoding='utf-8') as f:
        f.write(f"平均長度為 {audio_avg_length} 秒。")
        f.write(f"總數為 {audio_count} 個。")