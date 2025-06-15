#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# 添加Matcha-TTS到Python路径
sys.path.append('third_party/Matcha-TTS')

def test_cosyvoice():
    print("🧪 CosyVoice 功能测试")
    print("=" * 50)
    
    try:
        # 导入必要的模块
        print("📦 导入模块...")
        from cosyvoice.cli.cosyvoice import CosyVoice2
        import torchaudio
        print("✅ 模块导入成功")
        
        # 检查模型路径
        model_path = 'pretrained_models/CosyVoice2-0.5B'
        if not os.path.exists(model_path):
            print(f"❌ 模型路径不存在: {model_path}")
            return False
        
        print(f"📂 加载模型: {model_path}")
        
        # 加载模型（不启用JIT、TRT、VLLM以简化测试）
        cosyvoice = CosyVoice2(model_path, load_jit=False, load_trt=False, load_vllm=False, fp16=False)
        print("✅ 模型加载成功")
        
        # 测试文本转语音
        print("🎵 测试文本转语音...")
        test_text = "你好，这是CosyVoice的功能测试。"
        
        # 创建输出目录
        os.makedirs('test_output', exist_ok=True)
        
        # 执行SFT推理
        print("🔄 执行语音合成...")
        for i, j in enumerate(cosyvoice.inference_sft(test_text, '中文女')):
            output_file = f'test_output/test_sft_{i}.wav'
            torchaudio.save(output_file, j['tts_speech'], cosyvoice.sample_rate)
            print(f"💾 保存音频文件: {output_file}")
            
            if i >= 2:  # 只生成前3个片段
                break
        
        print("✅ 测试完成！")
        print("📁 输出文件保存在 test_output/ 目录中")
        return True
        
    except ImportError as e:
        print(f"❌ 模块导入错误: {str(e)}")
        print("💡 请确保已正确安装所有依赖和初始化子模块")
        return False
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

def main():
    success = test_cosyvoice()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 CosyVoice 测试成功！")
        print("📡 您现在可以:")
        print("   1. 访问 http://localhost:50000 使用Web界面")
        print("   2. 运行 python start_webui.py 重新启动Web界面")
        print("   3. 查看 test_output/ 目录中的生成音频")
    else:
        print("💔 测试失败，请检查错误信息")

if __name__ == "__main__":
    main() 