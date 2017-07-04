#encoding=utf8
import pickle
import copy
from itertools import combinations

def match(curriculum,myCourse):
	curriculum_need={1:{1:{},2:{},3:{},4:{},5:{}}, 2:{1:{},2:{}}, 3:{1:{},2:{},3:{1:{},2:{}},4:{}},4:{}}
	curriculum_have={1:{1:{},2:{},3:{},4:{},5:{}}, 2:{1:{},2:{}}, 3:{1:{},2:{},3:{1:{},2:{}},4:{}},4:{}}
	myCourse_copy=copy.deepcopy(myCourse)
	# 通识课程
	# 思政类
	course={}
	credit=0
	for key in curriculum[1][1]:
		if key in myCourse.keys():
			credit+=myCourse[key]
			curriculum_have[1][1][key]=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[1][1][key]
	if curriculum[1][1]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[1][1]['credit']-credit
	curriculum_have[1][1]['credit']=credit
	curriculum_need[1][1]=course
	
	# 军体类
	course={}
	credit=0
	for key in curriculum[1][2]:
		if key in myCourse.keys():
			credit+=myCourse[key]
			curriculum_have[1][2][key]=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[1][2][key]
	# 体育课
	course_del=[]
	credit2=0
	for key in myCourse:
		if '401' in key:
			curriculum_have[1][2][key]=myCourse[key]
			credit+=myCourse[key]
			credit2+=myCourse[key]
			course_del.append(key)
	for key in course_del:
		myCourse.pop(key)
	if credit2>=1:
		course.pop('031E0020')
		if credit2>=2:
			course.pop('031E0030')
			if credit2>=3:
				course.pop('031E0040')
				if credit2>=4:
					course.pop('031E0050')


	if curriculum[1][2]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[1][2]['credit']-credit

	curriculum_have[1][2]['credit']=credit
	curriculum_need[1][2]=course

	# 外语类
	course={}
	credit=0
	for key in curriculum[1][3]:
		if key in myCourse.keys():
			credit+=myCourse[key]
			curriculum_have[1][3][key]=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[1][3][key]
	if curriculum[1][3]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[1][3]['credit']-credit

	curriculum_have[1][3]['credit']=credit
	curriculum_need[1][3]=course

	# 计算机类
	course={1:{},2:{}}
	credit=0
	for key in curriculum[1][4][2]:
		if key in myCourse.keys():
			credit+=myCourse[key]
			curriculum_have[1][4][key]=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[1][4][2][key]
	

	credit2=0
	for key in curriculum[1][4][1][1]:
		if key in myCourse.keys():
			credit2+=myCourse[key]
			curriculum_have[1][4][key]=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[1][4][1][1][key]

	for key in curriculum[1][4][1][2]:
		if key in myCourse.keys():
			credit2+=myCourse[key]
			curriculum_have[1][4][key]=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[1][4][1][2][key]

	if curriculum[1][4][2]['credit']<=credit or curriculum[1][4][1]['credit']<=credit2:
		course={}
		course['credit_need']=0	
	else:
		course['credit_need']=min(curriculum[1][4][1]['credit']-credit2,curriculum[1][4][2]['credit']-credit)
	

	curriculum_have[1][4]['credit']=credit+credit2
	curriculum_need[1][4]=course

	# 通识选修类
	course={}
	credit=0
	credit_social=0
	courseS=False
	courseJ=False
	
	course_del=[]
	A={}
	for key in myCourse:
		if 'S' in key:
			curriculum_have[1][5][key]=myCourse[key]
			courseS=True
			credit+=myCourse[key]
			course_del.append(key)
		if 'K' in key:
			curriculum_have[1][5][key]=myCourse[key]
			credit+=myCourse[key]
			course_del.append(key)
		if 'M' in key:
			curriculum_have[1][5][key]=myCourse[key]
			credit+=myCourse[key]
			course_del.append(key)

		if 'J' in key:
			curriculum_have[1][5][key]=myCourse[key]
			courseJ=True
			credit_social+=myCourse[key]
			course_del.append(key)
		if 'H' in key:
			curriculum_have[1][5][key]=myCourse[key]
			credit_social+=myCourse[key]
			course_del.append(key)
		if 'I' in key:
			curriculum_have[1][5][key]=myCourse[key]
			credit_social+=myCourse[key]
			course_del.append(key)
		if 'L' in key:
			curriculum_have[1][5][key]=myCourse[key]
			credit_social+=myCourse[key]
			course_del.append(key)
		if 'A' in key:
			A[key]=myCourse[key]
	sorted_dict = sorted(A.items(), key=lambda A: A[1])
	list = sorted(A.values())
	final = 0
	final_index = []
	for i in range(len(list)):
		templist = combinations(range(len(list)), i)
		mintempA = []
		mintemx = []
		for x in templist:
			tempA=0
			for k in range(len(x)):
				tempA = tempA + list[x[k]]
			mintempA.append(tempA)
			mintemx.append(x)
		for t in range(len(mintempA)):
			if (6 - credit_social) - mintempA[t] + (7 - credit) <= 0:
				if final==0 or (6 - credit_social) - mintempA[t] + (7 - credit)>final:
					final=(6 - credit_social) - mintempA[t] + (7 - credit)
					final_index=mintemx[t]
	for index in final_index:
		curriculum_have[1][5][sorted_dict[index][0]] = sorted_dict[index][1]
		credit_social += sorted_dict[index][1]
		course_del.append(sorted_dict[index][0])
	for k in course_del:
		# print(k)
		myCourse.pop(k)
		

	curriculum_have[1][5]['credit']=credit+credit_social
	credit_need=(6-credit_social)+(7-credit)
	if credit_need<0:
		credit_need=0
	course['credit_need']=credit_need
	if not courseS:
		course['S类']='通识核心课程'
	if not courseJ:
		course['J类']='沟通领导类课程'
	curriculum_need[1][5]=course


	# 大类课程
	course={}
	credit=0
	for key in curriculum[2][1]:
		if key in myCourse.keys():
			curriculum_have[2][1][key]=myCourse[key]
			credit+=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[2][1][key]
	if curriculum[2][1]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[2][1]['credit']-credit

	curriculum_have[2][1]['credit']=credit
	curriculum_need[2][1]=course

	course={}
	credit=0
	for key in curriculum[2][2]:
		if key in myCourse.keys():
			curriculum_have[2][2][key]=myCourse[key]
			credit+=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[2][2][key]
	if curriculum[2][2]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[2][2]['credit']-credit
	curriculum_have[2][2]['credit']=credit
	curriculum_need[2][2]=course

	


	# 专业课程

	# 专业必修
	course={}
	credit=0
	# print( curriculum[3][1])
	for key in curriculum[3][1]:
		if key in myCourse.keys():
			curriculum_have[3][1][key]=myCourse[key]
			credit+=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[3][1][key]
	if curriculum[3][1]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[3][1]['credit']-credit
	curriculum_have[3][1]['credit']=credit
	curriculum_need[3][1]=course



	# 专业选修
	course={}
	credit=0
	# print( curriculum[3][2])
	for key in curriculum[3][2]:
		if key in myCourse.keys():
			curriculum_have[3][2][key]=myCourse[key]
			credit+=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[3][2][key]
	if curriculum[3][2]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[3][2]['credit']-credit
	curriculum_have[3][2]['credit']=credit
	curriculum_need[3][2]=course

	# 实践教学环节
	course={}
	credit=0
	for key in curriculum[3][3][1]:
		if key in myCourse.keys():
			curriculum_have[3][3][1][key]=myCourse[key]
			credit+=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[3][3][1][key]
	if curriculum[3][3][1]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[3][3][1]['credit']-credit
	curriculum_have[3][3][1]['credit']=credit
	curriculum_need[3][3][1]=course

	course={}
	credit=0
	for key in curriculum[3][3][2]:
		if key in myCourse.keys():
			curriculum_have[3][3][2][key]=myCourse[key]
			credit+=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[3][3][2][key]
	if curriculum[3][3][2]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[3][3][2]['credit']-credit

	curriculum_have[3][3][2]['credit']=credit
	curriculum_need[3][3][2]=course


	# 毕设
	course={}
	credit=0
	for key in curriculum[3][4]:
		if key in myCourse.keys():
			curriculum_have[3][4][key]=myCourse[key]
			credit+=myCourse[key]
			myCourse.pop(key)
		elif key != 'credit':
			course[key]=curriculum[3][4][key]
	if curriculum[3][4]['credit']<=credit:
		course={}
		course['credit_need']=0
	else:
		course['credit_need']=curriculum[3][4]['credit']-credit
	
	curriculum_have[3][4]['credit']=credit
	curriculum_need[3][4]=course


	# 个性课程
	credit=0
	for key in myCourse:
		if curriculum_need[3][2]<0:
			credit-=curriculum_need[3][2]['credit_need']
			curriculum_need[4]['overflow']=-curriculum_need[3][2]['credit_need']
			curriculum_need[3][2]['credit_need']=0
		credit+=myCourse[key]
		curriculum_have[4][key]=myCourse[key]
	curriculum_need[4]=myCourse
	curriculum_have[4]['credit']=credit
	curriculum_need[4]['credit_need']=curriculum[4]['credit']-credit
	
	curriculum_all={'curriculum_need':curriculum_need,'curriculum_have':curriculum_have}
	return curriculum_all


def show(dict):
	pass

if __name__=="__main__":
	input = open('curriculum.pkl', 'rb')
	curriculum = pickle.load(input)
	input.close()

	input = open('myCourse.pkl', 'rb')
	myCourse = pickle.load(input)
	input.close()

	print match(curriculum, myCourse)
	# dict={"curriculum_have": {"1": {"1": {"021E0040": 2.5, "021E0010": 2.5, "021E0020": 2.5, "credit": 12.5, "031E0031": 4.0, "371E0010": 1.0}, "2": {"credit": 7.5, "03110021": 2.0, "40101300": 1.0, "031E0010": 1.5, "40100101": 3.0}, "3": {"credit": 7.0, "051F0600": 1.0, "051F0020": 3.0, "051F0030": 3.0}, "4": {"211G0230": 2.0, "credit": 5.0, "211G0210": 3.0}, "5": {"201L0040": 1.5, "031I0020": 2.0, "611K0010": 1.5, "011L0080": 1.5, "credit": 11.0, "041S0260": 3.0, "011J0010": 1.5}}, "2": {"1": {"211D0130": 4.5, "061B0180": 2.0, "061B0190": 1.5, "061B0222": 3.0, "061B0170": 4.5, "061B0212": 3.0, "credit": 23.5, "211D0100": 5.0}, "2": {"081C0130": 2.5, "credit": 2.5}}, "3": {"1": {"21121350": 4.0, "21120510": 2.5, "21121300": 1.5, "credit": 41.5, "21191370": 2.0, "211C0020": 2.5, "21120350": 2.0, "21120920": 2.0, "21191051": 4.5, "211C0010": 2.5, "21191070": 2.0, "21121320": 2.5, "21121141": 3.0, "211B0010": 4.0, "21191320": 2.0, "21121340": 4.5}, "2": {"21121230": 2.0, "061B9090": 2.5, "21120491": 4.0, "21191360": 2.0, "061B0010": 1.0, "credit": 15.5, "21191590": 2.0, "21191100": 2.0}, "3": {"1": {"081C0251": 1.5, "credit": 6.5, "21120210": 2.5, "21120070": 2.5}, "2": {"credit": 0}}, "4": {"credit": 0}}, "4": {"credit": 2.5, "21120261": 2.5}}, "curriculum_need": {"1": {"1": {"credit_need": 1.0, "371E0020": "\u5f62\u52bf\u4e0e\u653f\u7b56\u2161"}, "2": {"03110080": "\u4f53\u8d28\u6d4b\u8bd5\u2160", "credit_need": 1.0, "03110090": "\u4f53\u8d28\u6d4b\u8bd5\u2161"}, "3": {"credit_need": 0}, "4": {"credit_need": 0}, "5": {"credit_need": 2.0}}, "2": {"1": {"credit_need": 0}, "2": {"credit_need": 0}}, "3": {"1": {"21120681": "\u4eba\u673a\u4ea4\u4e92\u6280\u672f**", "21190912": "\u8ba1\u7b97\u673a\u6e38\u620f\u7a0b\u5e8f\u8bbe\u8ba1**", "credit_need": 6.0}, "2": {"241C0010": "\u7cfb\u7edf\u79d1\u5b66\u4e0e\u5de5\u7a0b", "credit_need": 0.5, "111C0062": "\u4fe1\u53f7\u4e0e\u7cfb\u7edf\uff08\u4e59\uff09", "22120032": "\u8f6f\u4ef6\u5de5\u7a0b\u57fa\u7840", "21190040": "\u6570\u5b57\u5a92\u4f53\u8bbe\u8ba1", "21120161": "\u8ba1\u7b97\u673a\u8f85\u52a9\u5de5\u4e1a\u8bbe\u8ba1", "111C0070": "\u4fe1\u53f7\u4e0e\u7cfb\u7edf\u5b9e\u9a8c", "21121330": "\u64cd\u4f5c\u7cfb\u7edf**", "631B0010": "\u5de5\u7a0b\u6750\u6599", "061B0090": "\u504f\u5fae\u5206\u65b9\u7a0b", "21121270": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66\u7814\u7a76\u8fdb\u5c55", "21191441": "\u6570\u636e\u6316\u6398\u5bfc\u8bba", "21191581": "\u7f51\u7edc\u5b89\u5168\u539f\u7406\u4e0e\u5b9e\u8df5**", "21190640": "\u6570\u503c\u5206\u6790", "21191110": "\u4fe1\u606f\u68c0\u7d22\u548c", "21191030": "\u57fa\u4e8e GPU \u7684\u7ed8\u5236", "21120770": "\u52a8\u753b\u8bbe\u8ba1", "201A0050": "\u4e2d\u56fd\u5546\u4e1a\u6587\u5316\u4e0e\u521b\u4e1a\u7cbe\u795e"}, "3": {"1": {"credit_need": 0}, "2": {"credit_need": 2, "21188180": "\u6570\u5b57\u5a92\u4f53\u7efc\u5408\u5b9e\u8df5", "21191340": "\u6570\u5b57\u5a92\u4f53\u540e\u671f\u5236\u4f5c"}}, "4": {"credit_need": 8, "21189030": "\u6bd5\u4e1a\u8bbe\u8ba1\uff08\u8bba\u6587\uff09**"}}, "4": {"21120261": 2.5, "credit_need": 9.5}}}
	# show(dict)

