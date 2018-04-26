# -*- coding: utf-8 -*-
'''
>>> from opem.Static.Amphlett import *
>>> import random
>>> T=343.15
>>> PH2=1
>>> PO2=1
>>> i=0
>>> A=50.6
>>> l=0.178
>>> lambda_param=23
>>> N=1
>>> Jn=0.003
>>> JMax=0.469
>>> Enernst_Calc(T,PH2,PO2)
1.19075
>>> CH2_Calc(PH2,T)
7.330294784824117e-07
>>> CO2_Calc(PO2,T)
8.402541445801334e-07
>>> Rho_Calc(i,A,T,lambda_param)
4.978789826264977
>>> Xi2_Calc(A,PH2,T)
0.0030373688787134006
>>> Eta_Conc_Calc(i,A,Jn,JMax)
0
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
0
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
0
>>> PowerStack_Calc(2,2)
4
>>> PowerStack_Calc(None,2)
[Error] Power Stack Calculation Error (Power:None, N:2)
>>> T='20000000000'
>>> PH2='10000000'
>>> PO2='1000000000'
>>> i='160000000'
>>> A='30000000000'
>>> l='50000000000'
>>> lambda_param='50000000000'
>>> N='80000000000'
>>> Enernst_Calc(T,PH2,PO2)
[Error] Enernst Calculation Failed (T:20000000000 , PH2:10000000, PO2:1000000000)
>>> CH2_Calc(PH2,T)
[Error] CH2 Calculation Failed (PH2:10000000, T:20000000000)
>>> CO2_Calc(PO2,T)
[Error] CO2 Calculation Failed (PO2:1000000000, T:20000000000)
>>> Rho_Calc(i,A,T,lambda_param)
[Error] Rho Calculation Failed (i:160000000, A:30000000000, T:20000000000, lambda:50000000000)
>>> Xi2_Calc(A,PH2,T)
[Error] CH2 Calculation Failed (PH2:10000000, T:20000000000)
[Error] Xi2 Calculation Failed (A:30000000000, PH2:10000000, T:20000000000)
>>> Eta_Conc_Calc(i,A,None,None)
[Error] Eta Concentration Calculation Failed (i:160000000, A:30000000000, B:None, JMax:None)
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
[Error] Rho Calculation Failed (i:160000000, A:30000000000, T:20000000000, lambda:50000000000)
[Error] Eta Ohmic Calculation Failed (i:160000000, l:50000000000, A:30000000000, T:20000000000, lambda:50000000000, R_elec:None)
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
[Error] CO2 Calculation Failed (PO2:1000000000, T:20000000000)
[Error] CH2 Calculation Failed (PH2:10000000, T:20000000000)
[Error] Xi2 Calculation Failed (A:30000000000, PH2:10000000, T:20000000000)
[Error] Eta Activation Calculation Failed (T:20000000000, PO2:1000000000, PH2:10000000, i:160000000, A:30000000000)
>>> Efficiency_Calc(None)
[Error] PEM Efficiency Calculation Failed (Vcell:None)
>>> VStack_Calc(12,None)
[Error] VStack Calculation Error (N:12, Vcell:None)
>>> Amphlett_Data=Static_Analysis(InputMethod={},TestMode=True,PrintMode=False)
>>> Amphlett_Data["Status"]
False
>>> Loss_Calc(122,22,None)
[Error] Loss Calculation Error (Eta_Act:122, Eta_Ohmic:22, Eta_Conc:None)
>>> Vcell_Calc(122,None)
[Error] Vcell Calculation Error (Enernst:122, Loss:None)
>>> Vcell_Calc(122,None)
[Error] Vcell Calculation Error (Enernst:122, Loss:None)
>>> Test_Vector={"T":343.15,"PH2":1,"PO2":1,"i-start":0,"i-stop":4,"i-step":0.1,"A":50.6,"l":0.0178,"lambda":23,"N":1,"R":0,"JMax":1.5,"B":0.016,"Name":"test1"}
>>> Amphlett_Data=Static_Analysis(InputMethod=Test_Vector,TestMode=True)
###########
Amphlett-Model Simulation
###########
Analyzing . . .
I : 0
Enernst : 1.19075 V
Eta Activation : 0 V
Eta Concentration : 0 V
Eta Ohmic : 0 V
Loss : 0 V
PEM Efficiency : 0.763301282051282
Power : 0.0 W
Power-Stack : 0.0 W
Power-Thermal : 0.0 W
VStack : 1.19075 V
Vcell : 1.19075 V
###########
I : 0.1
Enernst : 1.19075 V
Eta Activation : 0.11807074742083559 V
Eta Concentration : 2.109426805213159e-05 V
Eta Ohmic : 0.00017520002843124318 V
Loss : 0.11826704171731897 V
PEM Efficiency : 0.6874890758222313
Power : 0.1072482958282681 W
Power-Stack : 0.1072482958282681 W
Power-Thermal : 0.015751704171731908 W
VStack : 1.072482958282681 V
Vcell : 1.072482958282681 V
###########
I : 0.2
Enernst : 1.19075 V
Eta Activation : 0.1639764642376006 V
Eta Concentration : 4.221638333089875e-05 V
Eta Ohmic : 0.0003505137928660484 V
Loss : 0.16436919441379755 V
PEM Efficiency : 0.6579364138373093
Power : 0.2052761611172405 W
Power-Stack : 0.2052761611172405 W
Power-Thermal : 0.0407238388827595 W
VStack : 1.0263808055862025 V
Vcell : 1.0263808055862025 V
###########
I : 0.3
Enernst : 1.19075 V
Eta Activation : 0.1908295871441327 V
Eta Concentration : 6.336641945755048e-05 V
Eta Ohmic : 0.0005259414221215358 V
Loss : 0.1914188949857118 V
PEM Efficiency : 0.6405968621886462
Power : 0.29979933150428645 W
Power-Stack : 0.29979933150428645 W
Power-Thermal : 0.06920066849571356 W
VStack : 0.9993311050142881 V
Vcell : 0.9993311050142881 V
###########
I : 0.4
Enernst : 1.19075 V
Eta Activation : 0.20988218105436562 V
Eta Concentration : 8.454445034568427e-05 V
Eta Ohmic : 0.0007014830568214833 V
Loss : 0.21066820856153282 V
PEM Efficiency : 0.628257558614402
Power : 0.3920327165753869 W
Power-Stack : 0.3920327165753869 W
Power-Thermal : 0.09996728342461313 W
VStack : 0.9800817914384672 V
Vcell : 0.9800817914384672 V
###########
I : 0.5
Enernst : 1.19075 V
Eta Activation : 0.22466052101362555 V
Eta Concentration : 0.00010575055020278165 V
Eta Ohmic : 0.0008771388470514419 V
Loss : 0.22564341041087976 V
PEM Efficiency : 0.618658070249436
Power : 0.4825532947945601 W
Power-Stack : 0.4825532947945601 W
Power-Thermal : 0.13244670520543989 W
VStack : 0.9651065895891202 V
Vcell : 0.9651065895891202 V
###########
I : 0.6
Enernst : 1.19075 V
Eta Activation : 0.23673530396089773 V
Eta Concentration : 0.00012698479353178086 V
Eta Ohmic : 0.0010529089510685316 V
Loss : 0.23791519770549804 V
PEM Efficiency : 0.610791539932373
Power : 0.5717008813767012 W
Power-Stack : 0.5717008813767012 W
Power-Thermal : 0.16629911862329885 W
VStack : 0.9528348022945019 V
Vcell : 0.9528348022945019 V
###########
I : 0.7
Enernst : 1.19075 V
Eta Activation : 0.2469443874769634 V
Eta Concentration : 0.000148247255132642 V
Eta Ohmic : 0.001228793534444728 V
Loss : 0.24832142826654077 V
PEM Efficiency : 0.60412087931632
Power : 0.6597000002134213 W
Power-Stack : 0.6597000002134213 W
Power-Thermal : 0.20129999978657856 W
VStack : 0.9424285717334592 V
Vcell : 0.9424285717334592 V
###########
I : 0.8
Enernst : 1.19075 V
Eta Activation : 0.25578789787113065 V
Eta Concentration : 0.00016953801010392253 V
Eta Ohmic : 0.0014047927694433354 V
Loss : 0.2573622286506779 V
PEM Efficiency : 0.5983254944546936
Power : 0.7467102170794577 W
Power-Stack : 0.7467102170794577 W
Power-Thermal : 0.23728978292054237 W
VStack : 0.933387771349322 V
Vcell : 0.933387771349322 V
###########
I : 0.9
Enernst : 1.19075 V
Eta Activation : 0.26358842686742984 V
Eta Concentration : 0.00019085713384438152 V
Eta Ohmic : 0.0015809068345387157 V
Loss : 0.2653601908358129 V
PEM Efficiency : 0.5931985956180685
Power : 0.8328508282477683 W
Power-Stack : 0.8328508282477683 W
Power-Thermal : 0.2741491717522317 W
VStack : 0.925389809164187 V
Vcell : 0.925389809164187 V
###########
I : 1.0
Enernst : 1.19075 V
Eta Activation : 0.2705662378303906 V
Eta Concentration : 0.00021220470205456714 V
Eta Ohmic : 0.0017571359140316743 V
Loss : 0.2725355784464768 V
PEM Efficiency : 0.5885989881753353
Power : 0.9182144215535232 W
Power-Stack : 0.9182144215535232 W
Power-Thermal : 0.3117855784464768 W
VStack : 0.9182144215535232 V
Vcell : 0.9182144215535232 V
###########
I : 1.1
Enernst : 1.19075 V
Eta Activation : 0.27687843565296244 V
Eta Concentration : 0.0002335807907384422 V
Eta Ohmic : 0.001933480197732536 V
Loss : 0.2790454966414334 V
PEM Efficiency : 0.5844259636913888
Power : 1.0028749536944233 W
Power-Stack : 1.0028749536944233 W
Power-Thermal : 0.3501250463055768 W
VStack : 0.9117045033585666 V
Vcell : 0.9117045033585666 V
###########
I : 1.2
Enernst : 1.19075 V
Eta Activation : 0.28264102077766273 V
Eta Concentration : 0.00025498547620500224 V
Eta Ohmic : 0.002109939880694226 V
Loss : 0.285005946134562 V
PEM Efficiency : 0.5806051627342551
Power : 1.0868928646385256 W
Power-Stack : 1.0868928646385256 W
Power-Thermal : 0.3891071353614744 W
VStack : 0.905744053865438 V
Vcell : 0.905744053865438 V
###########
I : 1.3
Enernst : 1.19075 V
Eta Activation : 0.28794208521933035 V
Eta Concentration : 0.0002764188350699048 V
Eta Ohmic : 0.002286515162983545 V
Loss : 0.2905050192173838 V
PEM Efficiency : 0.5770801158862924
Power : 1.1703184750174012 W
Power-Stack : 1.1703184750174012 W
Power-Thermal : 0.428681524982599 W
VStack : 0.9002449807826162 V
Vcell : 0.9002449807826162 V
###########
I : 1.4
Enernst : 1.19075 V
Eta Activation : 0.29285010429372843 V
Eta Concentration : 0.00029788094425712723 V
Eta Ohmic : 0.0024632062494824017 V
Loss : 0.29561119148746795 V
PEM Efficiency : 0.5738069285336743
Power : 1.2531943319175447 W
Power-Stack : 1.2531943319175447 W
Power-Thermal : 0.4688056680824551 W
VStack : 0.895138808512532 V
Vcell : 0.895138808512532 V
###########
I : 1.5
Enernst : 1.19075 V
Eta Activation : 0.29741936073692266 V
Eta Concentration : 0.00031937188100060893 V
Eta Ohmic : 0.002640013349713048 V
Loss : 0.3003787459676363 V
PEM Efficiency : 0.5707508038668997
Power : 1.3355568810485454 W
Power-Stack : 1.3355568810485454 W
Power-Thermal : 0.5094431189514546 W
VStack : 0.8903712540323636 V
Vcell : 0.8903712540323636 V
###########
I : 1.6
Enernst : 1.19075 V
Eta Activation : 0.3016936146878957 V
Eta Concentration : 0.0003408917228459314 V
Eta Ohmic : 0.0028169366776829123 V
Loss : 0.3048514430884245 V
PEM Efficiency : 0.567883690327933
Power : 1.417437691058521 W
Power-Stack : 1.417437691058521 W
Power-Thermal : 0.5505623089414792 W
VStack : 0.8858985569115755 V
Vcell : 0.8858985569115755 V
###########
I : 1.7
Enernst : 1.19075 V
Eta Activation : 0.3057086591103234 V
Eta Concentration : 0.00036244054765199196 V
Eta Ohmic : 0.0029939764517456784 V
Loss : 0.3090650761097211 V
PEM Efficiency : 0.5651826435194095
Power : 1.498864370613474 W
Power-Stack : 1.498864370613474 W
Power-Thermal : 0.5921356293865259 W
VStack : 0.8816849238902789 V
Vcell : 0.8816849238902789 V
###########
I : 1.8
Enernst : 1.19075 V
Eta Activation : 0.30949414368419487 V
Eta Concentration : 0.00038401843359268825 V
Eta Ohmic : 0.0031711328944759895 V
Loss : 0.3130492950122636 V
PEM Efficiency : 0.5626286570434207
Power : 1.5798612689779254 W
Power-Stack : 1.5798612689779254 W
Power-Thermal : 0.6341387310220746 W
VStack : 0.8777007049877363 V
Vcell : 0.8777007049877363 V
###########
I : 1.9
Enernst : 1.19075 V
Eta Activation : 0.3130749049111216 V
Eta Concentration : 0.00040562545915863245 V
Eta Ohmic : 0.003348406232555746 V
Loss : 0.31682893660283595 V
PEM Efficiency : 0.5602058098699769
Power : 1.6604500204546115 W
Power-Stack : 1.6604500204546115 W
Power-Thermal : 0.6765499795453883 W
VStack : 0.873921063397164 V
Vcell : 0.873921063397164 V
###########
I : 2.0
Enernst : 1.19075 V
Eta Activation : 0.3164719546471556 V
Eta Concentration : 0.0004272617031588504 V
Eta Ohmic : 0.0035257966966703337 V
Loss : 0.32042501304698484 V
PEM Efficiency : 0.5579006326621893
Power : 1.7406499739060304 W
Power-Stack : 1.7406499739060304 W
Power-Thermal : 0.7193500260939696 W
VStack : 0.8703249869530152 V
Vcell : 0.8703249869530152 V
###########
I : 2.1
Enernst : 1.19075 V
Eta Activation : 0.31970322720026056 V
Eta Concentration : 0.00044892724472251814 V
Eta Ohmic : 0.003703304521413451 V
Loss : 0.3238554589663965 V
PEM Efficiency : 0.5557016288676945
Power : 1.8204785361705675 W
Power-Stack : 1.8204785361705675 W
Power-Thermal : 0.7625214638294325 W
VStack : 0.8668945410336035 V
Vcell : 0.8668945410336035 V
###########
I : 2.2
Enernst : 1.19075 V
Eta Activation : 0.32278415246972747 V
Eta Concentration : 0.00047062216330069346 V
Eta Ohmic : 0.0038809299451994456 V
Loss : 0.3271357045782276 V
PEM Efficiency : 0.553598907321649
Power : 1.8999514499278993 W
Power-Stack : 1.8999514499278993 W
Power-Thermal : 0.8060485500721009 W
VStack : 0.8636142954217724 V
Vcell : 0.8636142954217724 V
###########
I : 2.3
Enernst : 1.19075 V
Eta Activation : 0.3257281015786805 V
Eta Concentration : 0.0004923465386680586 V
Eta Ohmic : 0.004058673210182234 V
Loss : 0.33027912132753073 V
PEM Efficiency : 0.5515838965849162
Power : 1.9790830209466792 W
Power-Stack : 1.9790830209466792 W
Power-Thermal : 0.8499169790533205 W
VStack : 0.8604708786724693 V
Vcell : 0.8604708786724693 V
###########
I : 2.4
Enernst : 1.19075 V
Eta Activation : 0.32854673759442776 V
Eta Concentration : 0.0005141004509246927 V
Eta Ohmic : 0.004236534562180054 V
Loss : 0.3332973726075325 V
PEM Efficiency : 0.5496491201233765
Power : 2.057886305741922 W
Power-Stack : 2.057886305741922 W
Power-Thermal : 0.8941136942580782 W
VStack : 0.8574526273924674 V
Vcell : 0.8574526273924674 V
###########
I : 2.5
Enernst : 1.19075 V
Eta Activation : 0.33125029460641553 V
Eta Concentration : 0.0005358839804978295 V
Eta Ohmic : 0.004414514250605397 V
Loss : 0.33620069283751874 V
PEM Efficiency : 0.5477880174118469
Power : 2.136373267906203 W
Power-Stack : 2.136373267906203 W
Power-Thermal : 0.9386267320937969 W
VStack : 0.8545493071624812 V
Vcell : 0.8545493071624812 V
###########
I : 2.6
Enernst : 1.19075 V
Eta Activation : 0.3338478020360954 V
Eta Concentration : 0.0005576972081436541 V
Eta Ohmic : 0.004592612528399569 V
Loss : 0.33899811177263856 V
PEM Efficiency : 0.5459948001457445
Power : 2.2145549093911394 W
Power-Stack : 2.2145549093911394 W
Power-Thermal : 0.9834450906088604 W
VStack : 0.8517518882273614 V
Vcell : 0.8517518882273614 V
###########
I : 2.7
Enernst : 1.19075 V
Eta Activation : 0.336347266590727 V
Eta Concentration : 0.0005795402149490941 V
Eta Ohmic : 0.004770829651971409 V
Loss : 0.3416976364576475 V
PEM Efficiency : 0.5442643356040721
Power : 2.292441381564352 W
Power-Stack : 2.292441381564352 W
Power-Thermal : 1.0285586184356483 W
VStack : 0.8490523635423525 V
Vcell : 0.8490523635423525 V
###########
I : 2.8
Enernst : 1.19075 V
Eta Activation : 0.33875582111049346 V
Eta Concentration : 0.0006014130823336223 V
Eta Ohmic : 0.00494916588113977 V
Loss : 0.34430640007396685 V
PEM Efficiency : 0.5425920512346366
Power : 2.3700420797928925 W
Power-Stack : 2.3700420797928925 W
Power-Thermal : 1.073957920207107 W
VStack : 0.8464435999260331 V
Vcell : 0.8464435999260331 V
###########
I : 2.9
Enernst : 1.19075 V
Eta Activation : 0.3410798472843882 V
Eta Concentration : 0.0006233158920510905 V
Eta Ohmic : 0.005127621479079398 V
Loss : 0.34683078465551875 V
PEM Efficiency : 0.5409738559900521
Power : 2.4473657244989955 W
Power-Stack : 2.4473657244989955 W
Power-Thermal : 1.1196342755010045 W
VStack : 0.8439192153444812 V
Vcell : 0.8439192153444812 V
###########
I : 3.0
Enernst : 1.19075 V
Eta Activation : 0.3433250775536877 V
Eta Concentration : 0.0006452487261915484 V
Eta Ohmic : 0.005306196712269878 V
Loss : 0.3492765229921491 V
PEM Efficiency : 0.5394060750050326
Power : 2.524420431023553 W
Power-Stack : 2.524420431023553 W
Power-Thermal : 1.1655795689764472 W
VStack : 0.8414734770078509 V
Vcell : 0.8414734770078509 V
###########
I : 3.1
Enernst : 1.19075 V
Eta Activation : 0.3454966803001176 V
Eta Concentration : 0.0006672116671831024 V
Eta Ohmic : 0.005484891850447433 V
Loss : 0.3516487838177481 V
PEM Efficiency : 0.537885394988623
Power : 2.6012137701649807 W
Power-Stack : 2.6012137701649807 W
Power-Thermal : 1.2117862298350193 W
VStack : 0.8391012161822519 V
Vcell : 0.8391012161822519 V
###########
I : 3.2
Enernst : 1.19075 V
Eta Activation : 0.3475993315046607 V
Eta Concentration : 0.0006892047977937692 V
Eta Ohmic : 0.00566370716655928 V
Loss : 0.35395224346901377 V
PEM Efficiency : 0.5364088182890937
Power : 2.677752820899156 W
Power-Stack : 2.677752820899156 W
Power-Thermal : 1.2582471791008443 W
VStack : 0.8367977565309862 V
Vcell : 0.8367977565309862 V
###########
I : 3.3
Enernst : 1.19075 V
Eta Activation : 0.34963727537625955 V
Eta Concentration : 0.0007112282011333409 V
Eta Ohmic : 0.005842642936720367 V
Loss : 0.35619114651411327 V
PEM Efficiency : 0.5349736240294146
Power : 2.7540442165034262 W
Power-Stack : 2.7540442165034262 W
Power-Thermal : 1.3049557834965735 W
VStack : 0.8345588534858868 V
Vcell : 0.8345588534858868 V
###########
I : 3.4
Enernst : 1.19075 V
Eta Activation : 0.35161437592708844 V
Eta Concentration : 0.0007332819606552831 V
Eta Ohmic : 0.00602169944017227 V
Loss : 0.358369357327916 V
PEM Efficiency : 0.5335773350462076
Power : 2.8300941850850854 W
Power-Stack : 2.8300941850850854 W
Power-Thermal : 1.3519058149149146 W
VStack : 0.8323806426720839 V
Vcell : 0.8323806426720839 V
###########
I : 3.5
Enernst : 1.19075 V
Eta Activation : 0.3535341610697534 V
Eta Concentration : 0.0007553661601586168 V
Eta Ohmic : 0.006200876959244138 V
Loss : 0.3604904041891562 V
PEM Efficiency : 0.5322176896223357
Power : 2.9059085853379534 W
Power-Stack : 2.9059085853379534 W
Power-Thermal : 1.3990914146620463 W
VStack : 0.8302595958108439 V
Vcell : 0.8302595958108439 V
###########
I : 3.6
Enernst : 1.19075 V
Eta Activation : 0.3553998605009599 V
Eta Concentration : 0.000777480883789843 V
Eta Ohmic : 0.0063801757793154595 V
Loss : 0.36255751716406515 V
PEM Efficiency : 0.5308926172025222
Power : 2.9814929382093656 W
Power-Stack : 2.9814929382093656 W
Power-Thermal : 1.4465070617906346 W
VStack : 0.8281924828359348 V
Vcell : 0.8281924828359348 V
###########
I : 3.7
Enernst : 1.19075 V
Eta Activation : 0.3572144383935416 V
Eta Concentration : 0.0007996262160448594 V
Eta Ohmic : 0.0065595961887805875 V
Loss : 0.36457366079836706 V
PEM Efficiency : 0.5296002174369442
Power : 3.056852455046042 W
Power-Stack : 3.056852455046042 W
Power-Thermal : 1.4941475449539583 W
VStack : 0.8261763392016329 V
Vcell : 0.8261763392016329 V
###########
I : 3.8
Enernst : 1.19075 V
Eta Activation : 0.35898062172788664 V
Eta Concentration : 0.0008218022417708932 V
Eta Ohmic : 0.0067391384790148525 V
Loss : 0.3665415624486724 V
PEM Efficiency : 0.5283387420200818
Power : 3.1319920626950446 W
Power-Stack : 3.1319920626950446 W
Power-Thermal : 1.5420079373049551 W
VStack : 0.8242084375513276 V
Vcell : 0.8242084375513276 V
###########
I : 3.9
Enernst : 1.19075 V
Eta Activation : 0.36070092494262745 V
Eta Concentration : 0.0008440090461684635 V
Eta Ohmic : 0.0069188029443421825 V
Loss : 0.36846373693313805 V
PEM Efficiency : 0.527106578889014
Power : 3.2069164259607614 W
Power-Stack : 3.2069164259607614 W
Power-Thermal : 1.5900835740392385 W
VStack : 0.8222862630668619 V
Vcell : 0.8222862630668619 V
###########
Done!

'''
