from utils import uploader
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
  handle = uploader().handle

  print(handle('/Users/ika/Desktop/9913509E9DE4492E0E903B4C2C66E98D.gif'))
  # print(handle('/Users/ika/Desktop/ACFC928140EE4FA072F4D6EB7CB35245.jpg'))
  # print(handle('/Users/ika/Desktop/out00006.ts'))
