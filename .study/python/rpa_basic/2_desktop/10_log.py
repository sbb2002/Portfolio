# import logging

# logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")    #디버그 레벨 이상 로그 설정
# # level 등급 이상, format 순서 작성시간, 레벨, 메세지
#
# #순서대로 점점 경고등급이 높아짐
# # debug < info < warning < error < critical
# logging.debug("아, 이거 누거 짠거야 ㅡㅡ")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 구닥다리야. 실행 상 문제가 있을 수 있다!")
# logging.error("에러 ㄷㄷㄷㅈ")
# logging.critical("장비를 정지합니다.")


# teminal and file에 log남기기
import logging
from datetime import datetime
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
#로그 레벨 설정
logger.setLevel(logging.DEBUG)

#스트림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

#파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")    # mylogfile_20210123011600.log
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")