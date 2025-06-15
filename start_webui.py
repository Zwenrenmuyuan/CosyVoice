#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse

def check_models():
    """检查模型是否存在"""
    model_paths = [
        'pretrained_models/CosyVoice2-0.5B',
        'pretrained_models/CosyVoice-300M',
        'pretrained_models/CosyVoice-300M-SFT',
        'pretrained_models/CosyVoice-300M-Instruct'
    ]
    
    available_models = []
    for path in model_paths:
        if os.path.exists(path):
            available_models.append(path)
            print(f"✅ 发现模型: {path}")
        else:
            print(f"❌ 模型不存在: {path}")
    
    return available_models

def main():
    print("🎤 CosyVoice Web界面启动器")
    print("=" * 50)
    
    # 检查可用模型
    available_models = check_models()
    
    if not available_models:
        print("❌ 没有找到可用的模型！")
        print("请先运行 'python download_models.py' 下载模型")
        return
    
    # 选择默认模型（优先选择CosyVoice2-0.5B）
    default_model = None
    if 'pretrained_models/CosyVoice2-0.5B' in available_models:
        default_model = 'pretrained_models/CosyVoice2-0.5B'
        print("🚀 使用CosyVoice2-0.5B模型（推荐）")
    elif 'pretrained_models/CosyVoice-300M' in available_models:
        default_model = 'pretrained_models/CosyVoice-300M'
        print("🚀 使用CosyVoice-300M模型")
    else:
        default_model = available_models[0]
        print(f"🚀 使用模型: {default_model}")
    
    print(f"📡 Web界面将在 http://localhost:50000 启动")
    print("=" * 50)
    
    # 启动Web界面
    try:
        import subprocess
        cmd = [sys.executable, 'webui.py', '--port', '50000', '--model_dir', default_model]
        print(f"执行命令: {' '.join(cmd)}")
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n👋 Web界面已关闭")
    except Exception as e:
        print(f"❌ 启动失败: {str(e)}")

if __name__ == "__main__":
    main() 