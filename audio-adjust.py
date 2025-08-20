import librosa
import soundfile
import pyrubberband
import os


Target = 180 #目标bpm ///target bpm
Tolerance = 50 # 原曲与目标bpm的差值，不建议修改/// difference of original bpm and target bpm, the modification is not recommended
inputpath = r"D:\temp work\Programme\Audio bpm adjust\base files" # 波形原始文件路径///original music file path 
outputpath = r"D:\temp work\Programme\Audio bpm adjust\output files" # 修改后文件储存路径+文件名///where you want to save the adjusted version + filename
# *导出文件默认为.wav格式，如要修改，则需要同时修改上面的后缀以及最后的subtype参数
# *output file is .wav format by default,change the extension above and subtype at the endline to change the file format*



def adjust_the_music_bpm(input,output,Target,Tolerance):

    # 读取原始文件
    # read the original file
    y, sr = librosa.load(input , sr=48000)
    tempo = librosa.beat.beat_track(y=y, sr=sr)[0]
    Bpm = round((tempo)[0],3)

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
    print(f'the original bpm of the song is:{Bpm}')

    # 修改歌曲速度匹配Target
    # strech the song to fit the target bpm
    AdjustRate = Target/FinalBpm
    StrechedResult = pyrubberband.time_stretch(y=y,sr=48000,rate=AdjustRate)
    print(f'Adjusted the song bpm by {AdjustRate:.2f} times')

    soundfile.write(output,StrechedResult,samplerate=48000)

os.makedirs(outputpath,exist_ok=True)

MusicNames = []
for files in os.listdir(inputpath):
    if os.path.isfile(os.path.join(inputpath,files)):
        MusicNames.append(files)
print(f"Found these files:\n{MusicNames}")

for i in MusicNames:
    inputfile = os.path.join(inputpath,i)
    outputfile = os.path.join(outputpath,f"Adjusted_{i}")
    adjust_the_music_bpm(inputfile,outputfile,Target,Tolerance)
    print(f'Finished process[{i}]')
    print('SUCCESSED')