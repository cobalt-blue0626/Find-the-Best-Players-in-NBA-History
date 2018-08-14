file=open("nba_data.csv","r")
data_space,data_name_year,data_name_year1=[],[],[]
i,j,h,k=0,0,0,0
#將資料轉為蜂巢串列並精簡資料
while i<21962:
	i=i+1
	data1=file.readline()
	data2=data1.split("\n")
	data3="".join(data2)
	data4=data3.split(",")
	data5=data4[1:4]+[data4[5]]+data4[7:]
	data_space.append(data5)
del data_space[0]

while j<21961:
	year,name1,name2=data_space[j][0],data_space[j][1],data_space[j][2]
	data_name_year,data_name_year1=data_name_year+[[year,name1,name2]],data_name_year1+[[year,name1,name2]]
	j=j+1
print(data_name_year)
h,a,p,po,r=0,0,0,0,0
po=[]
data_name_year_copy=data_name_year1[:]
#將相同在同一球季待過2個或以上球隊的球員資料作合併
while h<21961:
	year_check=data_name_year[h][0]
	name1_check=data_name_year[h][1]
	name2_check=data_name_year[h][2]
	data_name_year_check=[year_check,name1_check,name2_check]
	print(h,data_name_year_check)
	data_name_year_copy=data_name_year1[:]
	a,p,po,r=0,0,0,0
	while data_name_year_copy.count(data_name_year_check)>0 :
		a=data_name_year_copy.index(data_name_year_check)
		data_name_year_copy=data_name_year_copy[a+1:]
		p=p+a+1
		po=p-1
		if r!=0:
			data_space[h][3]=str(int(data_space[h][3])+int(data_space[po][3]))
			data_space[h][4]=str(int(data_space[h][4])+int(data_space[po][4]))
			data_space[h][5]=str(int(data_space[h][5])+int(data_space[po][5]))
			data_space[h][6]=str(int(data_space[h][6])+int(data_space[po][6]))
			data_space[h][7]=str(int(data_space[h][7])+int(data_space[po][7]))
			data_space[h][8]=str(int(data_space[h][8])+int(data_space[po][8]))
			data_space[h][9]=str(int(data_space[h][9])+int(data_space[po][9]))
			data_space[h][10]=str(int(data_space[h][10])+int(data_space[po][10]))
			data_space[h][11]=str(int(data_space[h][11])+int(data_space[po][11]))
			data_space[h][12]=str(int(data_space[h][12])+int(data_space[po][12]))
			data_space[h][13]=str(int(data_space[h][13])+int(data_space[po][13]))
			data_name_year[po][0]="0001"
			data_name_year[po][1]="None"
			data_name_year[po][2]="None"
			data_name_year[po][0]="0001"
			data_space[po][1]="None"
			data_space[po][2]="None"
			data_space[po][3]="1"
			data_space[po][4]="0"
			data_space[po][5]="0"
			data_space[po][6]="0"
			data_space[po][7]="0"
			data_space[po][8]="0"
			data_space[po][9]="0"
			data_space[po][10]="0"
			data_space[po][11]="0"
			data_space[po][12]="0"
			data_space[po][13]="0"
		print(" ",po,"po")
		r=r+1
	h=h+1
data_name_year1=data_space[:]
t=0
#計算每一季球員的當季效率值
while t<21961:
	eff_season=(int(data_space[t][4])+int(data_space[t][5])+int(data_space[t][6])+int(data_space[t][7])+int(data_space[t][8])-(int(data_space[t][10])-int(data_space[t][11])+int(data_space[t][12])-int(data_space[t][13])+int(data_space[t][9])))/int(data_space[t][3])
	data_space[t][0]="%.2f"%(eff_season)
	t=t+1
u=0
data_space_name=[]
while u<21961:
	data_space[u]=data_space[u][0:3]
	data_space_name+=[data_space[u][1:]]
	u=u+1
#將每位球員生涯每一季的當季效率值加總
g=0
while g<21961:
	n1,n2=data_space[g][1],data_space[g][2]
	n_check=[n1,n2]
	a,p,po,r=0,0,0,0
	data_space_name1=data_space_name[:]
	print(g,n_check)
	while data_space_name1.count(n_check)>0 and n1!="None":
		a=data_space_name1.index(n_check)
		data_space_name1=data_space_name1[a+1:]
		p=p+a+1
		po=p-1
		print(" ",po,"po")
		if r!=0:
			data_space[g][0]=str(float(data_space[g][0])+float(data_space[po][0]))
			print(data_space[g][0])
			data_space[po][1],data_space[po][2]="None","None"
		r=r+1
	g=g+1
data_space_new,m=[],0
while m<21961:
	if data_space[m][1]!="None":
		data_space_new+=[data_space[m][:]]
	m=m+1
data_name,rr=[],0
while rr<len(data_name_year1):
	data_name+=[data_name_year1[rr][1:3]]
	rr+=1
jj=0
#計算每位球員的生涯效率值
while jj<len(data_space_new):
	n1=data_space_new[jj][1]
	n2=data_space_new[jj][2]
	n_check=[n1,n2]
	data_space_new[jj][0]="%.2f"%(float(data_space_new[jj][0])/data_name.count(n_check))
	jj+=1
data_career,data_c=[],[]
#將生涯效率值由小排到大
yy=0
while yy<len(data_space_new):
	data_c.append(float(data_space_new[yy][0]))
	yy+=1
data_career=sorted(data_c,reverse=True)
qq=0
while qq<len(data_career):
	data_career[qq]="%.2f"%(data_career[qq])
	qq+=1
y=0
#將前20名的生涯效率值對應到相對的球員名字
while y<len(data_space_new):
	if data_space_new[y][0]==data_career[0]:
		print(data_space_new[y],"No.1")
		no_1=data_space_new[y][1]+" "+data_space_new[y][2]
		no_1_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[1]:
		print(data_space_new[y],"No.2")
		no_2=data_space_new[y][1]+" "+data_space_new[y][2]
		no_2_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[2]:
		print(data_space_new[y],"No.3")
		no_3=data_space_new[y][1]+" "+data_space_new[y][2]
		no_3_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[3]:
		print(data_space_new[y],"No.4")
		no_4=data_space_new[y][1]+" "+data_space_new[y][2]
		no_4_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[4]:
		print(data_space_new[y],"No.5")
		no_5=data_space_new[y][1]+" "+data_space_new[y][2]
		no_5_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[5]:
		print(data_space_new[y],"No.6")
		no_6=data_space_new[y][1]+" "+data_space_new[y][2]
		no_6_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[6]:
		print(data_space_new[y],"No.7")
		no_7=data_space_new[y][1]+" "+data_space_new[y][2]
		no_7_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[7]:
		print(data_space_new[y],"No.8")
		no_8=data_space_new[y][1]+" "+data_space_new[y][2]
		no_8_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[8]:
		print(data_space_new[y],"No.9")
		no_9=data_space_new[y][1]+" "+data_space_new[y][2]
		no_9_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[9]:
		print(data_space_new[y],"No.10")
		no_10=data_space_new[y][1]+" "+data_space_new[y][2]
		no_10_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[10]:
		print(data_space_new[y],"No.11")
		no_11=data_space_new[y][1]+" "+data_space_new[y][2]
		no_11_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[11]:
		print(data_space_new[y],"No.12")
		no_12=data_space_new[y][1]+" "+data_space_new[y][2]
		no_12_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[12]:
		print(data_space_new[y],"No.13")
		no_13=data_space_new[y][1]+" "+data_space_new[y][2]
		no_13_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[13]:
		print(data_space_new[y],"No.14")
		no_14=data_space_new[y][1]+" "+data_space_new[y][2]
		no_14_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[14]:
		print(data_space_new[y],"No.15")
		no_15=data_space_new[y][1]+" "+data_space_new[y][2]
		no_15_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[15]:
		print(data_space_new[y],"No.16")
		no_16=data_space_new[y][1]+" "+data_space_new[y][2]
		no_16_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[16]:
		print(data_space_new[y],"No.17")
		no_17=data_space_new[y][1]+" "+data_space_new[y][2]
		no_17_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[17]:
		print(data_space_new[y],"No.18")
		no_18=data_space_new[y][1]+" "+data_space_new[y][2]
		no_18_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[18]:
		print(data_space_new[y],"No.19")
		no_19=data_space_new[y][1]+" "+data_space_new[y][2]
		no_19_eff=data_space_new[y][0]
	elif data_space_new[y][0]==data_career[19]:
		print(data_space_new[y],"No.20")
		no_20=data_space_new[y][1]+" "+data_space_new[y][2]
		no_20_eff=data_space_new[y][0]
	y+=1
rank_output="Rank %d\t%20s\t%s\n"
print(rank_output%(1,no_1,no_1_eff))
print(rank_output%(2,no_2,no_2_eff))
print(rank_output%(3,no_3,no_3_eff))
print(rank_output%(4,no_4,no_4_eff))
print(rank_output%(5,no_5,no_5_eff))
print(rank_output%(6,no_6,no_6_eff))
print(rank_output%(7,no_7,no_7_eff))
print(rank_output%(8,no_8,no_8_eff))
print(rank_output%(9,no_9,no_9_eff))
print(rank_output%(10,no_10,no_10_eff))
print(rank_output%(11,no_11,no_11_eff))
print(rank_output%(12,no_12,no_12_eff))
print(rank_output%(13,no_13,no_13_eff))
print(rank_output%(14,no_14,no_14_eff))
print(rank_output%(15,no_15,no_15_eff))
print(rank_output%(16,no_16,no_16_eff))
print(rank_output%(17,no_17,no_17_eff))
print(rank_output%(18,no_18,no_18_eff))
print(rank_output%(19,no_19,no_19_eff))
print(rank_output%(20,no_20,no_20_eff))
#將最後的結果輸出
output=open("nba_best.txt","w")
output.write(rank_output%(1,no_1,no_1_eff))
output.write(rank_output%(2,no_2,no_2_eff))
output.write(rank_output%(3,no_3,no_3_eff))
output.write(rank_output%(4,no_4,no_4_eff))
output.write(rank_output%(5,no_5,no_5_eff))
output.write(rank_output%(6,no_6,no_6_eff))
output.write(rank_output%(7,no_7,no_7_eff))
output.write(rank_output%(8,no_8,no_8_eff))
output.write(rank_output%(9,no_9,no_9_eff))
output.write(rank_output%(10,no_10,no_10_eff))
output.write(rank_output%(11,no_11,no_11_eff))
output.write(rank_output%(12,no_12,no_12_eff))
output.write(rank_output%(13,no_13,no_13_eff))
output.write(rank_output%(14,no_14,no_14_eff))
output.write(rank_output%(15,no_15,no_15_eff))
output.write(rank_output%(16,no_16,no_16_eff))
output.write(rank_output%(17,no_17,no_17_eff))
output.write(rank_output%(18,no_18,no_18_eff))
output.write(rank_output%(19,no_19,no_19_eff))
output.write(rank_output%(20,no_20,no_20_eff))
output.close()
print("end")
file.close()