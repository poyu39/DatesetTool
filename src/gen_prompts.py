import os
import argparse


def get_prompts(label_path):
    output = []
    for file in os.listdir(label_path):
        with open(os.path.join(label_path, file), 'r', encoding='utf-8') as f:
            sub = f.readline()
            output.append((file, sub))
    return output

def gen_sub_txt(prompts, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for prompt in prompts:
            f.write(f"{str(prompt[0]).replace('.lab', '.wav')}|{prompt[1]}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--label_path', help='包含 .lab 檔案的資料夾路徑')
    args = parser.parse_args()
    prompts = get_prompts(args.label_path)
    gen_sub_txt(prompts, 'sub.txt')