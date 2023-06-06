# Encryption-and-Decryption-using-Python
Encrypting and Decrypting a text file using multiple methods

# <i> Encryption and Decryption </i>
# <u> Encryption & Decryption of Text files using Python </u>

## Description of Project:
- Here we're trying to encrypt the text files using Python, with multiple methods.
- Different metods used are :
    - Caesar Cipher
    - Brute Force.{Spcial case of Caeser Cipher used to get decrypted text of all possible outcomes.}
    -  Autokey_Cipher


## How to run this program :
- Clone my repository.
- Create  a text file need to be encrypted.
- Now run main file.
- Now select the option from different methods. 

    ### Caesar Cipher : 
    ```
    * Encrytion : 
    Please enter the method that you want to use:
    Brute Force is the special case of Caesar Cipher in which all the possible decrypted messages are displayed

          1. Caesar Cipher
          2. Brute Force
          3. Autokey Cipher
    Enter the choice: 1
    Enter 'E' if you want to encrypt the file or enter 'D' to decrypt the file : E
    Enter the name of the file that has to be encrypted : new
    Enter the key: 8
    Enter the name of the file that stores the encrypted data : Enc

    * Decryption : 
    Please enter the method that you want to use:
    Brute Force is the special case of Caesar Cipher in which all the possible decrypted messages are displayed

          1. Caesar Cipher
          2. Brute Force
          3. Autokey Cipher
    Enter the choice: 1
    Enter 'E' if you want to encrypt the file or enter 'D' to decrypt the file : D
    Enter key : 8
    Enter the name of the file that has to be decrypted : Enc
    Enter the name of the file that stores the decrypted data : Dec
    ```

    ### Brute force : 
    ```
    Please enter the method that you want to use:
    Brute Force is the special case of Caesar Cipher in which all the possible decrypted messages are displayed

          1. Caesar Cipher
          2. Brute Force
          3. Autokey Cipher

    Enter the choice: 2
    Enter the name of the file that has to be decrypted : Enc
    Decrypted text: 
    Key 0:Decrypted text: Pq Ug vium qa Ijpqapms B.
    Q'u i Kwuxcbmz Akqmvkm Abclmvb.
    Q'dm kwuxtmbml 6bp AMU.
    Twwsqvo nwz awum Qvbmzvapqxa.
    Key 1:Decrypted text: Op Tf uhtl pz Hiopzolr A.
    P't h Jvtwbaly Zjplujl Zabklua.
    P'cl jvtwslalk 6ao ZLT.
    Svvrpun mvy zvtl Pualyuzopwz.
    Key 2:Decrypted text: No Se tgsk oy Ghnoynkq Z.
    O's g Iusvazkx Yioktik Yzajktz.
    O'bk iusvrkzkj 6zn YKS.
    Ruuqotm lux yusk Otzkxtynovy.
    Key 3:Decrypted text: Mn Rd sfrj nx Fgmnxmjp Y.
    N'r f Htruzyjw Xhnjshj Xyzijsy.
    N'aj htruqjyji 6ym XJR.
    Qttpnsl ktw xtrj Nsyjwsxmnux.
    Key 4:Decrypted text: Lm Qc reqi mw Eflmwlio X.
    M'q e Gsqtyxiv Wgmirgi Wxyhirx.
    M'zi gsqtpixih 6xl WIQ.
    Pssomrk jsv wsqi Mrxivrwlmtw.
    Key 5:Decrypted text: Kl Pb qdph lv Deklvkhn W.
    L'p d Frpsxwhu Vflhqfh Vwxghqw.
    L'yh frpsohwhg 6wk VHP.
    Orrnlqj iru vrph Lqwhuqvklsv.
    Key 6:Decrypted text: Jk Oa pcog ku Cdjkujgm V.
    K'o c Eqorwvgt Uekgpeg Uvwfgpv.
    K'xg eqorngvgf 6vj UGO.
    Nqqmkpi hqt uqog Kpvgtpujkru.
    Key 7:Decrypted text: Ij Nz obnf jt Bcijtifl U.
    J'n b Dpnqvufs Tdjfodf Tuvefou.
    J'wf dpnqmfufe 6ui TFN.
    Mppljoh gps tpnf Joufsotijqt.
    Key 8:Decrypted text: Hi My name is Abhishek T.
    I'm a Computer Science Student.
    I've completed 6th SEM.
    Looking for some Internships.
    Key 9:Decrypted text: Gh Lx mzld hr Zaghrgdj S.
    H'l z Bnlotsdq Rbhdmbd Rstcdms.
    H'ud bnlokdsdc 6sg RDL.
    Knnjhmf enq rnld Hmsdqmrghor.
    Key 10:Decrypted text: Fg Kw lykc gq Yzfgqfci R.
    G'k y Amknsrcp Qagclac Qrsbclr.
    G'tc amknjcrcb 6rf QCK.
    Jmmigle dmp qmkc Glrcplqfgnq.
    Key 11:Decrypted text: Ef Jv kxjb fp Xyefpebh Q.
    F'j x Zljmrqbo Pzfbkzb Pqrabkq.
    F'sb zljmibqba 6qe PBJ.
    Illhfkd clo pljb Fkqbokpefmp.
    Key 12:Decrypted text: De Iu jwia eo Wxdeodag P.
    E'i w Ykilqpan Oyeajya Opqzajp.
    E'ra ykilhapaz 6pd OAI.
    Hkkgejc bkn okia Ejpanjodelo.
    Key 13:Decrypted text: Cd Ht ivhz dn Vwcdnczf O.
    D'h v Xjhkpozm Nxdzixz Nopyzio.
    D'qz xjhkgzozy 6oc NZH.
    Gjjfdib ajm njhz Diozmincdkn.
    Key 14:Decrypted text: Bc Gs hugy cm Uvbcmbye N.
    C'g u Wigjonyl Mwcyhwy Mnoxyhn.
    C'py wigjfynyx 6nb MYG.
    Fiiecha zil migy Chnylhmbcjm.
    Key 15:Decrypted text: Ab Fr gtfx bl Tuablaxd M.
    B'f t Vhfinmxk Lvbxgvx Lmnwxgm.
    B'ox vhfiexmxw 6ma LXF.
    Ehhdbgz yhk lhfx Bgmxkglabil.
    Key 16:Decrypted text: Za Eq fsew ak Stzakzwc L.
    A'e s Ugehmlwj Kuawfuw Klmvwfl.
    A'nw ugehdwlwv 6lz KWE.
    Dggcafy xgj kgew Aflwjfkzahk.
    Key 17:Decrypted text: Yz Dp erdv zj Rsyzjyvb K.
    Z'd r Tfdglkvi Jtzvetv Jkluvek.
    Z'mv tfdgcvkvu 6ky JVD.
    Cffbzex wfi jfdv Zekviejyzgj.
    Key 18:Decrypted text: Xy Co dqcu yi Qrxyixua J.
    Y'c q Secfkjuh Isyudsu Ijktudj.
    Y'lu secfbujut 6jx IUC.
    Beeaydw veh iecu Ydjuhdixyfi.
    Key 19:Decrypted text: Wx Bn cpbt xh Pqwxhwtz I.
    X'b p Rdbejitg Hrxtcrt Hijstci.
    X'kt rdbeatits 6iw HTB.
    Addzxcv udg hdbt Xcitgchwxeh.
    Key 20:Decrypted text: Vw Am boas wg Opvwgvsy H.
    W'a o Qcadihsf Gqwsbqs Ghirsbh.
    W'js qcadzshsr 6hv GSA.
    Zccywbu tcf gcas Wbhsfbgvwdg.
    Key 21:Decrypted text: Uv Zl anzr vf Nouvfurx G.
    V'z n Pbzchgre Fpvrapr Fghqrag.
    V'ir pbzcyrgrq 6gu FRZ.
    Ybbxvat sbe fbzr Vagreafuvcf.
    Key 22:Decrypted text: Tu Yk zmyq ue Mntuetqw F.
    U'y m Oaybgfqd Eouqzoq Efgpqzf.
    U'hq oaybxqfqp 6ft EQY.
    Xaawuzs rad eayq Uzfqdzetube.
    Key 23:Decrypted text: St Xj ylxp td Lmstdspv E.
    T'x l Nzxafepc Dntpynp Defopye.
    T'gp nzxawpepo 6es DPX.
    Wzzvtyr qzc dzxp Tyepcydstad.
    Key 24:Decrypted text: Rs Wi xkwo sc Klrscrou D.
    S'w k Mywzedob Cmsoxmo Cdenoxd.
    S'fo mywzvodon 6dr COW.
    Vyyusxq pyb cywo Sxdobxcrszc.
    Key 25:Encrypted text :  Pq Ug vium qa Ijpqapms B.
    Q'u i Kwuxcbmz Akqmvkm Abclmvb.
    Q'dm kwuxtmbml 6bp AMU.
    Twwsqvo nwz awum Qvbmzvapqxa.
    ```
    ### Autokey Cipher : 
    ```
    * Encryption : 
    Please enter the method that you want to use:
    Brute Force is the special case of Caesar Cipher in which all the possible decrypted messages are displayed

          1. Caesar Cipher
          2. Brute Force
          3. Autokey Cipher
    Enter the choice: 3
    To encrypt Then enter alphabet E or To decrypt Then enter alphabet D : E
    Enter the name of file that need to be encrypted : new
    Enter the autokey : Abhishek
    Enter the file where Autokey need to be saved : Auto
    Enter the file where encrypted text need to be saved : Encryption


    * Decryption : 
    Please enter the method that you want to use:
    Brute Force is the special case of Caesar Cipher in which all the possible decrypted messages are displayed

          1. Caesar Cipher
          2. Brute Force
          3. Autokey Cipher
          
    Enter the choice: 3
    To encrypt Then enter alphabet E or To decrypt Then enter alphabet D : D
    Enter the name of file that need to be decrypted : Encryption
    Enter the name of file that has Autokey : Auto
    Enter the file where decrypted text need to be saved : Decryption
    ```


```
Note : 

- Each encrypted file can be decrypted only using same method.

- And each time you need to do operations you need to restrart the program.
```

## Languages used : 
- Python


```
    --- THANK YOU ---
```
