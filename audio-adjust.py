# Beat tracking example
import librosa


# 1. 文件路径
filename = r"D:\temp work\Programme\Audio bpm adjust\base files\Requiem of fate.mp3"

# 2. 读取音频（保持原采样率）
y, sr = librosa.load(filename, sr=None)

# 3. 节拍检测
tempo = librosa.beat.beat_track(y=y, sr=sr)[0]


Bpm = round((tempo)[0],3)
Target = 180
Tolerance = 50

#如果bpm与180差距小于tolerance，则以原bpm作为处理素材，否则将原bpm*2或/2作为基础数据（即以原曲1/2拍作为一拍），如仍达不到需求则继续循环  
def adjust_bpm(bpm,target,tolerance):
    if abs(bpm - target) > tolerance:
        while bpm > target + tolerance:
            bpm /= 2
        while bpm < target - tolerance:
            bpm *=2
    return bpm
FinalBpm = adjust_bpm(Bpm,Target,Tolerance)



print(FinalBpm)