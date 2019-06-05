import preprocessing as pre 
# import read
# import check_dup as dup
# import allfunctions as func
# import fill

# /home/pwm4/Desktop/cg342/sleepprogram_redo/20190419/test2
# /home/pwm4/Desktop/cg342/sleepprogram_redo/20190530
# pathname = func.getInput()
# preprocessing data

def start(pathname):
    outputMessage = ""
    try:
        pre.preprocess(pathname)
        outputMessage += "\n"
        outputMessage += "\n Data preprocessing is successful\n"
    except:
        outputMessage += "\nData preprocessing error!\n"
    else:
        # run analysis
        outputMessage += "\n \nAnalyzing ...\n"
    
    return outputMessage