#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from modelscope import snapshot_download
import os

def download_model(model_id, local_dir):
    """下载单个模型"""
    print(f"🚀 开始下载模型: {model_id}")
    print(f"📁 保存到: {local_dir}")
    
    try:
        snapshot_download(model_id, local_dir=local_dir)
        print(f"✅ {model_id} 下载完成!")
        return True
    except Exception as e:
        print(f"❌ {model_id} 下载失败: {str(e)}")
        return False

def main():
    print("🎤 CosyVoice 模型下载器")
    print("=" * 50)
    
    # 创建模型目录
    os.makedirs('pretrained_models', exist_ok=True)
    
    # 要下载的模型列表
    models = [
        ('iic/CosyVoice2-0.5B', 'pretrained_models/CosyVoice2-0.5B'),
        ('iic/CosyVoice-300M', 'pretrained_models/CosyVoice-300M'),
        ('iic/CosyVoice-300M-SFT', 'pretrained_models/CosyVoice-300M-SFT'),
        ('iic/CosyVoice-300M-Instruct', 'pretrained_models/CosyVoice-300M-Instruct'),
        ('iic/CosyVoice-ttsfrd', 'pretrained_models/CosyVoice-ttsfrd'),
    ]
    
    success_count = 0
    total_count = len(models)
    
    for model_id, local_dir in models:
        if download_model(model_id, local_dir):
            success_count += 1
        print("-" * 50)
    
    print(f"📊 下载统计: {success_count}/{total_count} 模型下载成功")
    
    if success_count == total_count:
        print("🎉 所有模型下载完成！可以开始使用CosyVoice了！")
    else:
        print("⚠️ 部分模型下载失败，但核心模型可能已可用")

if __name__ == "__main__":
    main() 