import canlib.canlib as canlib
import time

def setUpChannel(channel=0,
                 openFlags=canlib.canOPEN_ACCEPT_VIRTUAL,
                 bitrate=canlib.canBITRATE_500K,
                 bitrateFlags=canlib.canDRIVER_NORMAL):
    cl = canlib.canlib()
    ch = cl.openChannel(channel, openFlags)
    print("Using channel: %s, EAN: %s" % (ch.getChannelData_Name(),
                                          ch.getChannelData_EAN()))
    ch.setBusOutputControl(bitrateFlags)
    ch.setBusParams(bitrate)
    ch.busOn()
    return ch


def tearDownChannel(ch):
    ch.busOff()
    ch.close()

cl = canlib.canlib()
print("canlib version: %s" % cl.getVersion())


channel_0 = 0

ch0 = setUpChannel(channel=0)

msgId = 0x4F1
msg = [0, 0, 0, 0,0,0,0x3F,0]
flg = canlib.canMSG_EXT
ch0.write(msgId, msg, flg)
tearDownChannel(ch0)
time.sleep(.01)
ch0 = setUpChannel(channel=0)
while True:
    try:
        (msgId, msg, dlc, flg, time) = ch0.read()
        data = ''.join(format(x, '02x') for x in msg)
        if msgId == 1280 :
             print("time:%9d id:%9d  flag:0x%02x  dlc:%d  data:%s" %
                  (time, msgId, flg, dlc, data))
        time.sleep(1)
    except :
        #time.sleep(0.1)
        pass

tearDownChannel(ch0)



/*
4f0 Host vehicle speed
4f0 vehicle yaw rate
4f0 yaw rate validity
4f1 scan index ack
4f1 lateral mounting offset
4f1 can misallignment
4f1 maximum tracks
4f1 cmd radiate
4f1 mmr upside down
4f1 vehicle speed validity
4f1 blockage disable
4f1 use angle misalignment
4f1 clear faults
4f1 high yaw angle
4f1 lr only transmit
4f1 mr only transmit
4f1 short track roc
5f2 radar fov mr
5f2 radar fov lr
5f2 auto allign disable
5f2 auto allign converged
5f2 align avg ctr total
5f2  AALIGN_AVG_CTR_TOTAL
5f2 serv align enable
5f2 serv align type
5f2 SERV_ALIGN_UPDATES_NEED
5f3 FAC_ALIGN_CMD_1
5f3 FAC_ALIGN_CMD_2
5f3 FAC_ALIGN_MAX_NT
5f3 FAC_ALIGN_SAMP_REQ
5f3 RX_FAC_TGT_MTG_OFFSET
5f3 FAC_TGT_MTG_SPACE_HOR
5f3 FAC_TGT_MTG_SPACE_VER
5f3 FAC_TGT_RANGE_1
5f3 FAC_TGT_RANGE_M2T
5f3 FAC_TGT_RANGE_R2M
5f4 OVERSTEER_UNDERSTEER
5f4 BEAMWIDTH_VERT
5f4 YAW_RATE_BIAS_SHIFT
5f4 FUNNEL_OFFSET_LEFT
5f4 FUNNEL_OFFSET_RIGHT
*/
