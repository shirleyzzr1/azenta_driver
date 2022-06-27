from sealer_client import A4S_SEALER_CLIENT

sealer1 = A4S_SEALER_CLIENT("/dev/ttyACM1")

sealer1.seal()
#sealer1.close_gate()



#Commands:
#Seal: *00GS=zz!
#Temperature Setting: *00DH=0100zz!
#Time Setting: *00DT=005zz!
#Shuttle Open: *00MO=zz!
#Shuttle Close: *00MC=zz!
#System Reset: *00SR=zz!

#*0MC=zz!, *00S=zz!, and *00DH=010zz! are should be incorrect commands but program thinks they are correct

#Correct command result
#*00MC=zz!
#b'*T01:26:12=0224,0,0,00,00,188,000GD!*Y00PM!\r'
#b'*T01:26:34=0224,0,0,00,00,188,000FP!*Y00PM!\r'
#b'*T01:27:06=0224,0,0,00,00,188,000FP!*Y00PM!\r'


#*00SR=zz!
#b'*D515A=0000272060,0000000000FL!*Y00PM!\r'
#b'*D515A=0000272088,0000000000FB!*Y00PM!\r'
#b'*T01:28:34=0224,0,0,00,00,188,000FN!*Y00PM!\r'

#*00DH=0100zz!
#b'*T01:29:09=0224,0,0,00,00,188,000FK!*Y00PM!\r'
#b'*T01:29:23=0432,0,2,00,00,188,000FL!*Y00PM!\r'
#b'*T01:29:31=0588,0,2,00,00,188,000FA!*Y00PM!\r'

#Incorrect but thought to be correct
#*0MC=zz!
#b'*T01:22:59=0224,0,0,00,00,188,000FM!*N01AG!*Y00PM!\r'
#b'*T01:23:18=0223,0,0,00,00,188,000GB!*N01AG!*Y00PM!\r'
#b'*T01:23:44=0224,0,0,00,00,188,000GB!*N01AG!*Y00PM!\r'

#*00S=zz!
#b'*T01:21:28=0224,0,0,00,00,188,000GB!*N00AH!*Y00PM!\r'
#b'*D515A=0000271701,0000000000FK!*N00AH!*Y00PM!\r'
#b'*T01:22:21=0224,0,0,00,00,188,000GH!*N00AH!*Y00PM!\r'

#*00DH=010zz!
#b'*D515A=0000271855,0000000000FA!*Y00PM!\r'
#b'*D515A=0000271869,0000000000EL!\r'
#b'*T01:25:06=0224,0,0,00,00,188,000GB!*Y00PM!\r'