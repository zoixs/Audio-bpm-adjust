import librosa
import soundfile
import pyrubberband

filename = r"D:\temp work\Programme\Audio bpm adjust\base files\Requiem of fate.mp3" # 波形原始文件路径///original music file path 
savepath = r"D:\temp work\Programme\Audio bpm adjust\base files\Requiem of fate adjust bpm version.wav" # 修改后文件储存路径+文件名///where you want to save the adjusted version + filename
# *导出文件默认为.wav格式，如要修改，则需要同时修改上面的后缀以及最后的subtype参数
# *output file is .wav format by default,change the extension above and subtype at the endline to change the file format*

# 读取原始文件
# read the original file
y, sr = librosa.load(filename, sr=48000)
tempo = librosa.beat.beat_track(y=y, sr=sr)[0]
Bpm = round((tempo)[0],3)
Target = 180 #目标bpm ///target bpm
Tolerance = 50 # 原曲与目标bpm的差值，不建议修改/// difference of original bpm and target bpm, the modification is not recommended

# 原始bpm修改
# change the original file's bpm
# 如果bpm与180差距小于tolerance，则以原bpm作为处理素材，否则将原bpm*2或/2作为基础数据（即以原曲1/2拍作为一拍），如仍达不到需求则继续循环
# if original bpm and target bpm's difference less than tolerance, use the original bpm, otherwise *2 or /2  
def adjust_bpm(bpm,target,tolerance):
    if abs(bpm - target) > tolerance:
        while bpm > target + tolerance:
            bpm /= 2
        while bpm < target - tolerance:
            bpm *=2
    return bpm
FinalBpm = adjust_bpm(Bpm,Target,Tolerance)

print(FinalBpm)

# 修改歌曲速度匹配Target
# strech the song to fit the target bpm
AdjustRate = Target/FinalBpm
StrechedResult = pyrubberband.time_stretch(y=y,sr=48000,rate=1.2)
print(type(StrechedResult))

soundfile.write(savepath,StrechedResult,samplerate=48000,subtype='PCM_24')
