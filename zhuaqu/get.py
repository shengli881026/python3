from urllib import request
import  json
'''
 * python 请求url 获取手机号号码的归属地查询
 *
'''
def get_url(tel):
    url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel='+ tel
    req = request.urlopen(url)
    page = req.read()
    ret = page.decode('gbk')
    if(req.getcode() == 200):
        return ret
    else:
        return -1
    #return page
# 请求url 获取手机号归属地
tel_phone_list = ['13462169727','15203868185','13903418770','13351229688','13838041266','13253345139','15800328096','18098736022','13693862293','15961264692','15056783222','15565065131','15262032313','15879529453','18212999385','13881840559','15377149889','15178086055','13730834463','15138478756','15083862973','13314308165','18937485580','18226082926','15929466111','18103705000','13607638177','15873970919','15209023250','13739851186','19807798726','13935980716','13700816688','15238660769','13366245039','15104365577','15835990391','13903853657','18623324716','18560636970','15504839939','15262059292','18052277908','13785623587','13782385007','13995281059','18636137878','15947430524','13968029318','15802979359','18837627709','15177350135','14703477666','13603188258','15303719698','13015519828','18172335255','13965807099','13569421004','13939428785','13503946492','15551988362','13646736866','15999079681','18239845612','18954855567','15961197826','13937314265','13333866861','13213409333','18937112983','13814273373','13401622580','13401352876','13961160202','13885885879','13387679015','13956737370','13966518813','15056879129','15253423227','18793042333','13659309799','18193061886','18671887826','15293893589','18293009292','18704547726','13091847409','18653295008','13634752604','13645216384','15862155286','13722154951','13523558011','13838098165','13561263839','13073738834','15162074859','13937089970','17783629360','18265959456','15807731393','15038188253','15840115391','18605188882','18351236134','13665478306','18251628998','15203355559','15252233862','15168749555','15538983330','15134444344','13994207908','18625536668','18693554758','13131491319','13703821430','15036632780','13515256969','18135637702','13817298971','13912322990','13338188557','13685227598','13954853234','13862695050','15252255505','13209004111','13813686879','18915839197','13938762455','15852737357','15042695988','13613769806','18047594123','13425307575','13956706551','18739592727','13338968111','13999720675','18729139676','13729264275','18293540179','15393389959','18703840633','15868533520','18348546987','13603769698','13935325158','13527370058','13581217168','13781530377','13526534181','15865712177','18952125759','13239920288','13781502101','13137663699','18227262761','18275070906','18832832165','18623884503','13598614513','13569883338','18225833782','15996617538','13705673758','17756751535','13966850322','18537131521','13173251777','13140031009','18236537511','13956680487','18056700294','15022317556','15359933160','18646157366','18502301997','18677936949','15603185181','13932889353','15138571800','13953388988','15951233880','13831818811','15809451568','18522767449','18226075288','15842162825','15256775977','18109678252','13721427675','13693737242','13965552236','15255912866','13952228522','13566076009','18089491010','15252218880','18609962459','13509792057','15210541237','13937254884','17703868159','13884554915','13689459912','15303769358','15803978881','13998818561','13653818412','18239929075','13566570875','13777128883','18339015850','13513988938','13281026177','15318069368','15945096107','15382229786','13703759689','18342022238','15683508060','18778899415','13855152298','17353911341','13676999107','13869157650','18395219758','13667951597','13531223616','13231015033','15733091765','15542180195','13639665583','18133367355','17839795736','13882022822','15097218067','13956042788','13937734068','13673812097','13683704866','15236028588','15303746539','15044243888','15290619198','18286052802','15591700500','13952465550','18631217025','13892789579','15846859817','15139070758','13636293388','13775811744','13402750818','18005213370','18234067749','13649552391','13837015466','13653190155','18270176661','13873295445','18756789419','13166075516','15305200065','15055816718','18967697222','18137779039','13991757162','18538575254','18069338093','18169777390','18236983573','13781573097','13901502353','15861161728','15061950677','13955826329','18689230212','13907327737','18973225399','18195175435','13992482178','15162135861','13736768777','18878774555','18537642211','18118493117','13855880393','18737618886','13732127778','15238311999','15725316390','13724923368','18198056720','15239540103','18626026859','18839550828','15019624698','15005678096','18767169285','18937421116','15162149164','15839033197','13992330263','18749146129','15868379383','15137344833','15836159301','13100013007','13462241893','13730136995','15556755289','13363488314','13225108161','18655802152','13937956385','13700610451','15838228202','13569481750','15639972800','18931135477','15857833901','18637507068','15389893399','18003746039','15565593311','15988926168','15305225266','15162241114','15238297333','18906321659','13600680206','15996877828','13932406702','18865331237','13785943393','13503792000','15051334488','13673863996','13703941841','13330656128','13646755093','18003716318','13996540448','15555256080']
str_dict = {'__GetZoneResult_ = ':'','mts':'"mts"','province':'"province"','catName':'"catName"','telString':'"telString"','areaVid':'"areaVid"','ispVid':'"ispVid"','carrier':'"carrier"'}

for tel in tel_phone_list:
    ret = get_url(tel)
    #n_str = ret.replace('__GetZoneResult_ = ','')
    for key,val in str_dict.items():
        ret = ret.replace(key,val)
    ret = ret.replace("'",'"')
    dict_ret = json.loads(ret)
    if dict_ret is not None:
        print(tel,',',dict_ret['province'])
