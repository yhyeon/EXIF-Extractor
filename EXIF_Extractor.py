#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PIL import Image
from struct import *

import piexif


from collections import defaultdict


# 사진 EXIF 정보 추출 함수 정의

def GPS(imgs):
	#Image.open(imgs)._getexif()[34853]
	v = piexif.load(imgs)
	
	gv = (v["GPS"])

	lr = str(gv[1]).split("'")[1]
	l1 = float(gv[2][0][0]) / float(gv[2][0][1])
	l2 = float(gv[2][1][0]) / float(gv[2][1][1])
	l3 = float(gv[2][2][0]) / float(gv[2][2][1])
	lgr = str(gv[3]).split("'")[1]
	lt1 = float(gv[4][0][0]) / float(gv[4][0][1])
	lt2 = float(gv[4][1][0]) / float(gv[4][1][1])
	lt3 = float(gv[4][2][0]) / float(gv[4][2][1])
	return ("{0} {1}°{2}＇{3}˝, {4} {5}°{6}＇{7}˝".format(lr,l1,l2,l3,lgr,lt1,lt2,lt3))
	

def DateTime(imgs):
	return str(Image.open(imgs)._getexif()[306])
def DateTimeOriginal(imgs):
	return str(Image.open(imgs)._getexif()[36867])
def DateTimeDigitized(imgs):
	return str(Image.open(imgs)._getexif()[36868])

def Make(imgs):
	return str(Image.open(imgs)._getexif()[271])
def Model(imgs):
	return str(Image.open(imgs)._getexif()[272])
def ExifVersion(imgs):
	value = (Image.open(imgs)._getexif()[36864])
	return unpack("<L", value)

def FNumber(imgs):
	v = (Image.open(imgs)._getexif()[33437])
	return v[0]/v[1]
def WhiteBalance(imgs):
	return str(Image.open(imgs)._getexif()[41986])
def ExposureProgram(imgs):
	return str(Image.open(imgs)._getexif()[34850])
def ExposureMode(imgs):
	return str(Image.open(imgs)._getexif()[41986])
def ExposureTime(imgs):
	v = (Image.open(imgs)._getexif()[33434])
	return ("{0}/{1}".format(v[0],v[1]))

def ExposureBiasValue(imgs):
	v = (Image.open(imgs)._getexif()[37380])
	return v[0]/v[1]

def ShutterSpeedValue(imgs):
	v = (Image.open(imgs)._getexif()[37377])
	return v[0]/v[1]

def BrightnessValue(imgs):
	v = (Image.open(imgs)._getexif()[37379])
	return v[0]/v[1]

def MeteringMode(imgs):
	return str(Image.open(imgs)._getexif()[37383])

def FlashPixVer(imgs):
	v = str(Image.open(imgs)._getexif()[40960])
	return v.split("'")[1]


def Flash(imgs):
	return str(Image.open(imgs)._getexif()[37385])
def FocalLength(imgs):
	v = (Image.open(imgs)._getexif()[37386])
	return v[0]/v[1]

def ISOSpeedRatings(imgs):
	return str(Image.open(imgs)._getexif()[34855])

def SubsecTime(imgs):
	return str(Image.open(imgs)._getexif()[37520])
def SubsecTimeOriginal(imgs):
	return str(Image.open(imgs)._getexif()[37521])
def SubsecTimeDigitized(imgs):
	return str(Image.open(imgs)._getexif()[37522])


def SceneCaptureType(imgs):
	return str(Image.open(imgs)._getexif()[41990])
def SceneType(imgs):
	v = Image.open(imgs)._getexif()[41729]
	v = v[0]
	#return ord(v)
	return v

def YCbCrPositioning(imgs):
	return str(Image.open(imgs)._getexif()[531])

def ColorSpace(imgs):
	return str(Image.open(imgs)._getexif()[40961])
def PixelXDimension(imgs):
	return str(Image.open(imgs)._getexif()[40962])
def PixelYDimension(imgs):
	return str(Image.open(imgs)._getexif()[40963])

def DigitalZoomRatio(imgs):
	v = (Image.open(imgs)._getexif()[41988])
	return v[0]/v[1]

def SensingMethod(imgs):
	return str(Image.open(imgs)._getexif()[41495])

def ComponentsConfiguration(imgs):
	v = (Image.open(imgs)._getexif()[37121])
	v0 = v[0]
	v1 = v[1]
	v2 = v[2]
	v3 = v[3]
	if v[0] is 1:
		a = "Y"
	if v[1] is 2:
		b = "Cb"
	if v[2] is 3:
		c = "Cr"
	if v[3] is 0:
		d = "-"
	return a, b, c, d


def UserComment(imgs):
	v = (Image.open(imgs)._getexif()[37510])
	return str(v)[2:-1]


def MakerNote(imgs):
	v = str(Image.open(imgs)._getexif()[37500])
	return v.split("'")[1]




# EXIF 정보 테이블 클래스 정의

class full_new(QTableWidget):
	def __init__(self):
		super().__init__()

		if imgs == []: # 이미지 선택 안 되었을 경우
			self.pause = True # 해당 클래스 실행 멈춤
		else: # 이미지 선택되었을 경우
			self.initUI() # 클래스의 initUI 함수 실행


	def initUI(self):
		self.resize(500, 700) # 창 크기 지정
		self.setWindowTitle('EXIF Full Extractor') # 창 타이틀 지정
		self.move(505, 95) # 창 위치 설정
		global imgs_num #imgs_num 전역 변수 선언
		imgs_num = int(len(imgs)) # imgs_num은 imgs 값 개수

		row = ['GPS', 'DateTime', 'DateTimeOriginal', 'DateTimeDigitized', 'Make', 'Model', 'ExifVersion', 'FNumber', 'WhiteBalance', 'ExposureProgram', 'ExposureMode', 'ExposureTime', 'ExposureBiasValue', 'ShutterSpeedValue', 'BrightnessValue', 'MeteringMode', 'FlashPixVer', 'Flash','FocalLength', 'ISOSpeedRatings', 'SubsecTime','SubsecTimeOriginal','SubsecTimeDigitized', 'SceneCaptureType', 'SceneType', 'YCbCrPositioning', 'ColorSpace','PixelXDimension','PixelYDimension', 'DigitalZoomRatio', 'SensingMethod','ComponentsConfiguration', 'UserComment', 'MakerNote']
		# row = EXIF 목록

		global rnum # rnum 전역변수 선언
		rnum = int(len(row)) #rnum은 row 값 개수

		self.setRowCount(rnum) # rnum만큼 테이블 row 생성
		self.setColumnCount(int(imgs_num)) # imgs_num만큼 테이블 column 생성

		self.setVerticalHeaderLabels(row) # row 값을 각 row 헤더 이름으로 설정
		self.setHorizontalHeaderLabels(imgs) # imgs 값을 각 column 헤더 이름으로 설정 

		self.resizeColumnsToContents() # 컨텐츠에 맞게 column 크기 조정


		for i in range(imgs_num): # imgs_num 범위의 i 동안
			# 아래 함수 값을 토대로 테이블 생성
			self.setItem(0,i, QTableWidgetItem("{0}".format(GPS(imgs[i]))))
			self.setItem(1,i, QTableWidgetItem("{0}".format(DateTime(imgs[i]))))
			self.setItem(2,i, QTableWidgetItem("{0}".format(DateTimeOriginal(imgs[i]))))
			self.setItem(3,i, QTableWidgetItem("{0}".format(DateTimeDigitized(imgs[i]))))
			self.setItem(4,i, QTableWidgetItem("{0}".format(Make(imgs[i]))))
			self.setItem(5,i, QTableWidgetItem("{0}".format(Model(imgs[i]))))
			self.setItem(6,i, QTableWidgetItem("{0}".format(ExifVersion(imgs[i]))))
			self.setItem(7,i, QTableWidgetItem("{0}".format(FNumber(imgs[i]))))
			self.setItem(8,i, QTableWidgetItem("{0}".format(WhiteBalance(imgs[i]))))
			self.setItem(9,i, QTableWidgetItem("{0}".format(ExposureProgram(imgs[i]))))
			self.setItem(10,i, QTableWidgetItem("{0}".format(ExposureMode(imgs[i]))))
			self.setItem(11,i, QTableWidgetItem("{0}".format(ExposureTime(imgs[i]))))
			self.setItem(12,i, QTableWidgetItem("{0}".format(ExposureBiasValue(imgs[i]))))
			self.setItem(13,i, QTableWidgetItem("{0}".format(ShutterSpeedValue(imgs[i]))))
			self.setItem(14,i, QTableWidgetItem("{0}".format(BrightnessValue(imgs[i]))))
			self.setItem(15,i, QTableWidgetItem("{0}".format(MeteringMode(imgs[i]))))
			self.setItem(16,i, QTableWidgetItem("{0}".format(FlashPixVer(imgs[i]))))
			self.setItem(17,i, QTableWidgetItem("{0}".format(Flash(imgs[i]))))
			self.setItem(18,i, QTableWidgetItem("{0}".format(FocalLength(imgs[i]))))
			self.setItem(19,i, QTableWidgetItem("{0}".format(ISOSpeedRatings(imgs[i]))))
			self.setItem(20,i, QTableWidgetItem("{0}".format(SubsecTime(imgs[i]))))
			self.setItem(21,i, QTableWidgetItem("{0}".format(SubsecTimeOriginal(imgs[i]))))
			self.setItem(22,i, QTableWidgetItem("{0}".format(SubsecTimeDigitized(imgs[i]))))
			self.setItem(23,i, QTableWidgetItem("{0}".format(SceneCaptureType(imgs[i]))))
			self.setItem(24,i, QTableWidgetItem("{0}".format(SceneType(imgs[i]))))
			self.setItem(25,i, QTableWidgetItem("{0}".format(YCbCrPositioning(imgs[i]))))
			self.setItem(26,i, QTableWidgetItem("{0}".format(ColorSpace(imgs[i]))))
			self.setItem(27,i, QTableWidgetItem("{0}".format(PixelXDimension(imgs[i]))))
			self.setItem(28,i, QTableWidgetItem("{0}".format(PixelYDimension(imgs[i]))))
			self.setItem(29,i, QTableWidgetItem("{0}".format(DigitalZoomRatio(imgs[i]))))
			self.setItem(30,i, QTableWidgetItem("{0}".format(SensingMethod(imgs[i]))))
			self.setItem(31,i, QTableWidgetItem("{0}".format(ComponentsConfiguration(imgs[i]))))
			self.setItem(32,i, QTableWidgetItem("{0}".format(UserComment(imgs[i]))))
			self.setItem(33,i, QTableWidgetItem("{0}".format(MakerNote(imgs[i]))))

			self.horizontalHeaderItem(i).setTextAlignment(Qt.AlignRight) # column 헤더 우측 정렬


		for j in range(rnum): # rnum 범위의 j동안
			self.verticalHeaderItem(j).setTextAlignment(Qt.AlignCenter) # row 헤더 가운데 정렬

# 이미지 분석 클래스 정의

class Analysis(QWidget):
	def __init__(self):
		super().__init__()

		if imgs == []: # 이미지 선택 안 되었을 경우
			self.pause = True # 클래스 실행 멈춤
		else: # 이미지 선택되었을 경우
			self.initUI() # initUI 실행

		self.resize(500, 700) # 창 크기 설정
		self.move(1000, 95) # 창 위치 설정

	def initUI(self):
		self.setWindowTitle('Img Analysis') # 창 타이틀 설정
		dic = dict() # dic 딕셔너리 정의
		orip = dict() # orip 딕셔너리 정의
		for i in range(imgs_num): # imgs_num 범위의 i 동안
			# 각 함수 값과 매칭하는 변수 정의
			img = imgs[i]
			gps = (GPS(imgs[i]))
			dt = (DateTime(imgs[i]))
			dto = (DateTimeOriginal(imgs[i]))
			dtd = (DateTimeDigitized(imgs[i]))
			make = (Make(imgs[i]))
			model = (Model(imgs[i]))
			ev = (ExifVersion(imgs[i]))
			fnum = (FNumber(imgs[i]))
			wb = (WhiteBalance(imgs[i]))
			ep = (ExposureProgram(imgs[i]))
			em = (ExposureMode(imgs[i]))
			et = (ExposureTime(imgs[i]))
			ebv = (ExposureBiasValue(imgs[i]))
			ssv = (ShutterSpeedValue(imgs[i]))
			bv = (BrightnessValue(imgs[i]))
			mm = (MeteringMode(imgs[i]))
			fpv = (FlashPixVer(imgs[i]))
			f = (Flash(imgs[i]))
			fl = (FocalLength(imgs[i]))
			iso = (ISOSpeedRatings(imgs[i]))
			subt = (SubsecTime(imgs[i]))
			subto = (SubsecTimeOriginal(imgs[i]))
			subtd = (SubsecTimeDigitized(imgs[i]))
			scap = (SceneCaptureType(imgs[i]))
			stype = (SceneType(imgs[i]))
			ycb = (YCbCrPositioning(imgs[i]))
			cols = (ColorSpace(imgs[i]))
			pix = (PixelXDimension(imgs[i]))
			pixy = (PixelYDimension(imgs[i]))
			dzoom = (DigitalZoomRatio(imgs[i]))
			smethod = (SensingMethod(imgs[i]))
			comconf = (ComponentsConfiguration(imgs[i]))
			ucomt = (UserComment(imgs[i])[5:10])
			mknote = (MakerNote(imgs[i])[2])
			dic[img] = (make,model,ucomt) # dic 딕셔너리에 img 값을 keys로, make, model, ucomt 값을 values로 입력

			if dt == dto == dtd: # dt와 dto와 dtd 값이 같다면
				if ucomt == '\\x00\\': # ucomt 값이 \\x00\\인 경우
					orip[dt] = (img) # orip 딕셔너리에 dt 값을 keys로, img 값을 values로 입력
				


		v = defaultdict(list) # defaultdictionary 생성
		for key, value in sorted(dic.items()): # 정렬된 dic 딕셔너리의 key와 value마다
			v[value].append(key) # unique 값을 갖는 keys를 그룹화하여 리스트 생성한 후 v 딕셔너리에 입력

		keys = v.values() # v 딕셔너리의 values를 값으로 갖는 keys 변수 정의


		clsbtn = QPushButton('Close', self) # Close 버튼 생성
		clsbtn.setToolTip('Close this programme') # 버튼 툴팁 정의
		clsbtn.resize(50, 20) # 버튼 크기 지정
		clsbtn.move(240, 8) # 버튼 위치 지정

		clsbtn.clicked.connect(self.close) # 버튼 클릭 시 창 종료되도록 설정

		layout = QVBoxLayout() # QVBoxLayout 속성의 layout 정의
		layout.addWidget(clsbtn) # close 버튼 레이아웃에 추가
		mLayout = QGridLayout() # QGridLayout 속성의 mLayout 정의
		mLayout.addLayout(layout,0,1) # mLayout에 layout 추가
		self.setLayout(mLayout) # mLayout으로 레이아웃 설정

		self.text = QTextEdit() # QTextEdit 속성의 self.text 정의
		layout.addWidget(self.text) # self.text 위젯을 layout에 추가

		self.text.setReadOnly(True) # 텍스트창 read only 설정

		output = "Images grouped by: {0}\r\rOrigianl Images: {1}".format(v.values(), orip.values())
		# 텍스트창 입력 문구 지정 (v.values와 orip.values을 각각 이미지 그룹핑, 원본 이미지 이름으로 출력)
		
		self.text.setText(output) # output을 텍스트창에 출력



class Initial(QWidget): # 메인 클래스 정의

	global imgs # imgs 전역 변수 정의
	imgs = [] # imgs 값 초기화

	def imgsup(self):
		options = QFileDialog.Options() # QFileDialog.Options 속성의 options 정의
		options |= QFileDialog.DontUseNativeDialog
		files, _ = QFileDialog.getOpenFileNames(None,"OpenFile", "","All Files (*)") # 확장자 관계 없이 다수 파일 오픈 기능

		if files: # 파일 존재 (선택) 시
			global imgs
			imgs = files # 파일 값을 imgs 변수에 입력
			return Initial.initUI(self) # initUI 실행
	
		else: # 파일 미존재 시
			QMessageBox.about(self, "Cancelled", "Please select images.") # 이미지 선택하라는 메시지박스 출력
			return Initial.imgsup(self) # 파일 선택창으로 반환


	def __init__(self):
		super().__init__()

		self.initUI()


	def initUI(self):
	
		QToolTip.setFont(QFont('NanumBarunGothic', 14)) # 툴팁 폰트 설정

		self.setToolTip('This is a <b>EXIF Extrator</b> Prgrogramme') # 툴팁 메시지 설정

		clsbtn = QPushButton('Close', self) # Close 버튼 생성
		clsbtn.setToolTip('Close this programme') # 버튼 툴팁 메시지 지정
		clsbtn.resize(50, 20) # 버튼 크기 지정
		clsbtn.move(240, 8) # 버튼 위치 지정
		clsbtn.clicked.connect(self.close) # 버튼 클릭 시 창 종료

		imgsupbtn = QPushButton('1. Select Images', self) # 이미지 선택 버튼 생성
		imgsupbtn.setToolTip('Select your images') # 버튼 툴팁 메시지 지정
		imgsupbtn.resize(280, 30) # 버튼 크기 지정
		imgsupbtn.move(10, 60) # 버튼 위치 지정
		imgsupbtn.clicked.connect(self.imgsup) # 버튼 클릭 시 imgsup 함수 실행

		fullbtn = QPushButton('2. Full EXIF Info', self) # 이미지 EXIF 정보 테이블 버튼 생성
		fullbtn.setToolTip('Full EXIF Extracting Mode') # 버튼 툴팁 메시지 지정
		fullbtn.resize(135, 25) # 버튼 크기 지정
		fullbtn.move(10, 120) # 버튼 위치 지정
		fullbtn.clicked.connect(self.on_pushButton_clicked1) # 버튼 클릭 시 on_pushButton_clicked1 함수 실행
		self.dialog1 = full_new() # 실행할 클래스는 full_new 클래스

		selbtn = QPushButton('2. Analysis', self) # 분석 버튼 생성
		selbtn.setToolTip('Analysing EXIF Info') # 버튼 툴팁 메시지 지정
		selbtn.resize(135, 25) # 버튼 크기 지정
		selbtn.move(155, 120) # 버튼 위치 지정
		selbtn.clicked.connect(self.on_pushButton_clicked) # 버튼 클릭 시 on_pushButton_clicked 함수 실행
		self.dialog = Analysis() # 실행할 클래스는 Analysis 클래스

		self.setWindowTitle('EXIF Extractor') # 창 타이틀 지정

#		self.show() # 창 실행


	def on_pushButton_clicked1(self): 
		self.dialog1.show() # self.dialog1 함수 실행



	def on_pushButton_clicked(self):
		self.dialog.show() # self.dialog 함수 실행


if __name__ == '__main__':

	app = QApplication(sys.argv)

	w = Initial() # Initial 클래스 실행
	w.resize(300, 180) # 창 크기 지정
	w.move(200, 100) # 창 위치 지정
	w.setWindowTitle('EXIF Extrator') # 창 타이틀 지정
	w.show() # 실행

	sys.exit(app.exec_())
