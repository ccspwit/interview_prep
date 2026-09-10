# -*- coding: utf-8 -*-
"""
Created on Sun May 14, 2017
LeetCode problem 387
Given a string, find the first non-repeating character in it and return
it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
@author: K Li
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        Use counter, save (count, index)
        min(index) for count==1
        """
        #charSet = set(s)

        charCount = {}
        # create charater count dictionary
        for ind, ch in enumerate(s):
            charCount[ch] = (charCount.get(ch,(0,0))[0]+1, ind)
        
        """minIndex = len(s)
        for count, ind in charCount.values():
            if (count==1) & (ind<minIndex):
                minIndex = ind
        return minIndex if minIndex < len(s) else -1"""
        indices = [ind for cnt, ind in charCount.values() if cnt==1]
        if indices:
            return min(indices)
        else:
            return -1

    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        Use counter, save (count, index)
        min(index) for count==1
        """
        #charSet = set(s)

        charCount = {}
        # create charater count dictionary
        for ind, ch in enumerate(s):
            charCount[ch] = (charCount.get(ch,(0,0))[0]+1, ind)
        
        """minIndex = len(s)
        for count, ind in charCount.values():
            if (count==1) & (ind<minIndex):
                minIndex = ind
        return minIndex if minIndex < len(s) else -1"""
        indices = [ind for cnt, ind in charCount.values() if cnt==1]
        if indices:
            return min(indices)
        else:
            return -1

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        Use counter, scan twice
        """
        #charSet = set(s)

        charCount = {}
        # create charater count dictionary
        for ch in s:
            charCount[ch] = charCount.get(ch,0)+1
        
        for ind, ch in enumerate(s):
            if charCount[ch]==1:
                return ind
        return -1

    def firstUniqCharTLE(self, s):
        """
        :type s: str
        :rtype: int
        Use str.count, Time Limit Exceeded!
        count is O(n) operation
        """
        #charSet = set(s)
        index = -1
        for ind, ch in enumerate(s):
            #print(ch)
            if s.count(ch)==1:
                return ind

        return -1

if __name__ == '__main__':
    a = Solution()
    testVector = ["","aa","heart","leetcode","loveleetcode",
                  "fmjiooebgjatqjttfftvobormhubvgxpiobekkxujgvaktcewbvkdnqwqme"]
    a = Solution()
    for test in testVector:
        print(test)
        print("%s -- %s"%(test, a.firstUniqChar(test)))
        print("%s -- %s"%(test, a.firstUniqChar1(test)))

    test="fmjiooebgjatqjttfftvobormhubvgxpiobekkxujgvaktcewbvkdnqwqmeeaogpcgaliilvimtsqtlfnhtvvipwsesosgluwtpearpvrrlpjgppqgegejsruiwbnppnlonpsetvfverxhmtihrfcbspupgmhrqniosmosamujoxqdepvjrcnhgqmkuhrlbrwmwtldfjnnkjnvpfonuvpewusqxstgxcfikmcwcgkipootlemscowhstxcaefreafjfxtuqcbdvasncmijmvdjlwcqopxnxdwqafwugelnuwledeajbkvjilvbjkarimpesekhmoixfapihomeswgirtovrgjgarjglnjmshirxphafbghvxuwpxggpbkewemvtrrmjxscdjlfvnfuepqkjffkkmdcstaktwlwawxcpxdgxsidxmcnhhlrtpmqfafucwxdieasfjgueridmakgcehmqtehwbkvahedxscsniwpdannvbpobtskdgmpfijknlunawajfcrgvigbkrlmuonuubmaluqfsjvsajjixbqjqrvwbhebumwsjvmqovawxjqbrumpdttswmqmutdvqvvtujmkbdauckvdcfknhsrwxxaucfqhabuinedmrocivwmhtwlkvfuqjmnouvkquijisidwqoekheegfvxxvdcngjxrjtlxfcgufmcjvtxrjuhipeoenouagigobxjfcpblvirfjvtfbhdmrjpqpvsxhijumbfjehswteajcmqhcdbstolecqlktajmtrhmjddnoawocbohrjqlgckhhhrkbcwgvpxolrlhwuvebsumijspknesmsspcvibsemoccjndalknqlxguvwvhbeujhavjpflwpuexgwwmbaqmlqdilwbaixemaokwsdppqjtgkdgixhkmmoixssvatqguvqjuctwfpvpjulmuuprkobuhkasxabjxvhltaejkuxoxopojcxxnasxcnqwnqsngktxdbhpuxacxgpgfxieeubcgkulklslskdwvimqvpatdvkukejojafuvqbrpqkcbwpohesnmvgpsdqoordplnhnoacwsabsvwjbcujvrrcimqcolvnwckgfbkuuvuqmfjohxrkamlnfrmaexcqeordnwwclgsxpibbgetfwntxpbocgeguaxavmnlkbpkvdamhqlsriuqhempogbsicviftokeiowlreddnlfxvblgpcxhtgovkijdbbtjavfihmwtldogomedftgdwlkkbjlwgogjplgfqimhevlhcntxqaukoqoqoowxkntlxxkbrihahqvsrmikphqvdfrgjarngpkaptrfmufovumglkcdcjeefsmndqnrjccpqwcaiuhifbptjftksxownppntulkdqujrapdfqfxhhqssxbjophmsusfrgarnxawkjwgeqhsdgvlggvvodgwfcvvgexwgrofdsiquvuscopwoewjlkndexhgripagmggvbfswngxlpgrjxwcmtcdbmrqsrhhgchkhxntaklapsshhrdljaghmstcspinnctbkuhuukevmfcwqjgcsqjhtxnnqrsxttisubvusprxurqwnpxxatdkifxbmrnirhxghmnuixbwppcigtwusjmrddqvowawffxntxqeauojlfrebmdwrkttsqsjpiebknsvgqwdrvgbkvebqnnpeorbpwlogqssfhorkbgkukkomvnaktvhtfwkbmeumuqridupxasqacshphkippegghkprknspngnckmatxiwfhnevkvkqjhtwvvqganrsdogtswdavjtuifwfwuwmjjgknwuaowbkpwoemsbvcvalvqfqlpteqjqsqpuhewrbxacurhbtwmuexpanjajomgbhhwpmswbonkndhwubjvixmcamivcegbaqjmwoigsrhffchxrhdcmdfjmnaitohcgfvaaohnmthqkakkrfmrhaslnbbhxkwrkxvuoknvollvfnxpeemtkgmctplllsknnfxwhetmjbnkosnvjtlpeojmniwtswvxopfpmeklmfeqmgovbscpwxdktstjcuwioowhvibkqaqxirbptkhbpbiegaqllgngvbkgjsxqmrrhbuglqcmoincrgppswdjjsqrejcohbrxpqofrhspwbsqlkrgotemlfllqewnnppkrvxgbrlsbrijatuphrifkqtiltillftkdhpjkwedxihhrrdanjhfiihivgxkbenxwgxgffnexiibgltthtjslaamoemjxtwbslgfkgxulwchwjwhwnpvugmswvwiflnbwwfojtbtbnwrteumskqgskvducfhklkvmgksjjlqbtlpluljtimvxvdabdbohewgkuxxedovvarbpifibqutbhepwhtnmvqfbhugqhijuvqhhbrqtjxojpkcapsvjarqbqpqgneefkjsdoqskdnqxgnxkkwewcprbpclggpxbolqsaamwqphdttqlbidsnuhltnbpclaacpsoxdxhgmfmxgukmxdgrxrnngblqxacvljvcrlvvejebvsacmkcnjbamhkibdhgajtijbqaoalrsjufdvswkbwejxgxeioosjkpnlhpipkecjrjjmrcipqbdxmqkflqurfjghwlnrqnqnjdrqjnwtpwtgedssivnltqtwpecgudvgenwsrjuodfiuohnqdfpoocvhicrxoqakcvfjqedxuulbkgcgghhlnqesdekdockldurnapthceeoigtuanhrqshxpmvlnkkrqkqhiktnovccaindinxqphgxmqborqbdphswaemrowwgttcsqapicjscjrwedegjrcrcqpgdljpqprkrxwvcjglwihfvlvstpmktqrxuweolnamqfxevupqfarwccunchfxcrtkdfasmwsrakcscducgbrakgrwndnawjfnakvenifrigaiqgnicdfenbegujmnxjormlclvnktrbjfpojdhworurfuqtsnwravocjrmdixkdvrpbkdhleaoiujaqwackjcooalserxlnegbjwpcahqdfifmxrpmkspuoqdaptamnobemgxpggkmqcpmctkkllvbubrgmhfgucnimkmogcgxikhbquaodetfxduclvtalriwxjopgedxpigsbtkxmmswhnvwlfvkitsvhfudisjbeeuqnchgnmswujerogjfvquntepjkukhpnqkmxaswecmwnqeejxiqawodxpboetaiudiwlutgudawkbndpqdtkprwwtetahvhjekuwmchmulsqqpuvuhvxqvoadqibmuvmubmhifiuoedgfppwssoxadspiaxhchavtuhqppbtqubohxujlxosqskjsrpscwrditgpknlklbnghoefgleiqspxqnasuhradhxnqjebovnpvuvdmasaptprdtcghfgcnxeckcnacidjacbdnfquvgtpkefamvcswtdgxqoxxiouixwnalesecliwobgcilxgmoiieinmhfxwtorfahtbhigpuorsxtttresmvbtkuklkhqgvgrgwgqhmlnidsjeasukmdkjqamadsloqfcndovuffevwpmldiarixmphklwcejpnmdgaxfflbewtaoieshhxiwnxkxvwfbsfdstekcboxoujuwtuabdswxlpbivqwdwhsrkpodkfqahiuuelkwpisrahngnxwpnmswdctpojduxkhikarojsldfqrbgugnveclifsqwkaruuvkwemrkirvckkbipvnxwshxhsnsxqgvrosrouqkrvxhukwdplhltkbsjtgbisntxdjixhjqvvrthiahfilrstlxcflfowfwodvgxpvovmdiseqdinsrmmuhtrmurmgwhwxcvufsjhfegpeibbscqgurewbxavalkvidcmxvaipiliwohufnhadxuvkweqdeohgknrvhtgrmapevthbcakjxduijmgxsmfthwlfqjrlpwfqvnjqreewkkwjpbguvdnnkxqjpdcgtmravecqklhcqjaokdacfmbokocawjqqgtdwgqdleesgrxeaarmsswifblabdsttbcebrldqqagimnrfkddstcdrfhdohwuvuccjlcsxwobrldhxqcedsabmhscokhcqxsiohijxgxvceiofbgxgvxkfgtnbtcvsbttamdgsikcbimxgpgfbvqpemsvxusgftnfhjduxmqgahqcualvocswraraqdnmifpnthjiwrjlnimvgfvpttwcubfiebththkemgfeximjcnpcuotukcdavqrfugviwrnqcowxtbjowmkiocndcvksnvdogbsvjdjdopubiecmrouiuduetnchshttlumjuennoirlximstlwropaxvcupnismuvirpfkutkserxsbelxlmhqvqtathoisxfrhcohcgfcumxcquvigolfvmcncgcueommsvpvhfbpecbehlkjtutoirvmeeupshsecriubkojdrfjwrdbjhoefpnmcxminughquitsudrrtsrggnrifwxuwkglrbamekflpadsdkhposlwkdqjijgfwejhafopoexdlqtpwjcmetpwnmptoabbqcwhgwlwmnnrgqudxbdauophihnoblrpkvfssfhsfewmcqgnvrjmotjajnldxrgxfwnqukbsjdlewaawqtfxckfcswrjcepskchjmechqilcbpsnafhjasutjcoarkfhqmkwsvrqkvpvngncnagkqnfvirtbueawgdxwglhvhaonrfjfxektcbbpgkxtscxiwonkipdgqjjcnenhxjmdwpassgdonlkuhwfiqbgutsqvrkkhdpmtuhrngnwcurkcbdwspbpobscnfjpnenrjvqnqjpbaxkpstnradwxetiadrxnktumphldmdulxppavxmgrvjwhxnronnmnweuntrehmuvicigcmxmfoklwhjworllwxvsjkaaumghbbvickieemjhbreglwilgexgnsrwqdlamefhecfnprgbrhncoswtuhrpjflgvrdrrustacgauersnavjggtdahngdkijkpwroxctglfmwmbbftvnldiftmbcnjgxhtlbnhophnbkslppccdtoafpmfgewjwpfweqokoasjjskqtekupvgmcjluldpuaclbhppsrwpvwtftfpqrtllrouqqkixruqrknwcgbiptiweenjrbvuogsqujjsgariqdwupvehbrxswtcjpuojosoewakcejqsxdbrejdlvbkalivartpclpcipltisekhoraxtbolmslhldofievwvuwgvdelpbvhwhjtdfmxvdaapufrkqdnnbsedqhemrjbwmfivnpiqwstwekurpxikoncotccpcqggiumxjngfkbpjjefncdpntirishglfafgtvpurxinpeeounumhfbvqtqixuxfdkxhvksbvnhpnvdpwdkaighkwgagqrwpcwlagbvighsumsuuvpxrtnautrbdpasamescodhakestmuwdlaknkunuqdsgcavaaeumnirrkwxuwdcwhimwubobgvehdamxfnqolqcextqpqximivndjvkltxwgjrjwvbhqbllqhefndppwaqevaiblbrjeulenhoqtnilfebhvqfhlwjbltsfigdvieweslfuoaadefjoxvxbtsqnvjdtkmnjljjshjfkjldtmrgrmegnxmnitccokcgfetwwtjqdfebcvkgjdlbkfmpbogqmpppslclhxtexjfkiixcwumsbicqbfoffbnaaqwrvrxcnfvnhdikxavpjvgopbajkitjwuxpruvcocmtmrnfmgaktoqbujfetfrbfgghtnfurhbespwvgwejhsrlqnfnpphkmgrxswxaxmwixplqvrreurxtsnbwwpnkufbbxwevpbshlimhifhfcutqskxncmmsfkxlsnsmcpvaxsbkavgdssotstrtqgsswgrgkutnhvpflwsruoonudwmhivplvqbihbrpkfapmqeodilvcxmpandesntrcorkhwocxcfckbwqsbccarauikphpifcunaevhtdujdxkqsdrxmnavattusisowpdtpikwjjqrthrgkncqkddbglkvsqqogaqcgmfcqftmvjrduwnwegagameuaodcnecivaodawvrjgbqrpqprwhfxprbuucbdurptffbafxixvrtrhfndkjedujmfhgthxwgbtdmsrijhpcgeatpidnfmkvnnjwisoifxbpeulreaudisxlnbrlxcceukckjuahtnhsbhdbjttmaswuwokmrulprnssmnotklhtudiqqamnqgvoeojxntwfmwqhcnafbjgstxdwshihheecgluuspdwnueqdlnuaohppndmfxxkvejwmdeeiijsnrpniaobitidjtrrccrmsqhehpqfhoqcsljxpvkdhqrvxcensoexopemvxbshacfgljvkhccovtftkvjtmdcriqnxtgiipedxjqxhbnwvsgutcmuxuuwlunpfcqbsmbnhvnwikeinwjrjmawevxjedqkqwounmwkuobrerphmkfmewrqebwnmvuhwnbjrsokigtithvtdobvtjjrgwgsujwfrqjrxnxnkdmmumovlkgnqnvrknkwcrrmxhflnmjucoutjidutgemccaqpgxuptlnsjohninpaxcqbluikkkabxqpxrareamxratgfbdeefgimeqscvqdfwfgjntgaavkdkfphxsvoscnkeqbcihewfadveqeckoocadsrjdbgmtwelmfsdxlvvjquuqtuiguvcganrvqmmmlartokohbiwhumwlrnaoeuhgakfbticdnponnkiafixkxgcqqutnuxjkkawxrcwqlrbljkdrancucchqxtjugwwlpxewldxugplntsndiqvkebxcxbklrrxioxwghbwxupmkjchwxhbxfjqpxwfrfqmshiwrxgeqhdmlgcbjveorwudpxsdolunasssudagaxblxpsceawtaoiibxfutsdjdavdcjrhgkljpwlercesvfxwvqqaitossibralpwtcqntctffsabimhhebrpmewogkwmjbmcwoaqkdmglbjbassbglbjipjoxpvltbheihlkfcehjwxcwhxvcebvemjcugeawviebualtgfipbkmrugtrgxuhbvrwaurtupkafbcmhfqolcpkahttjnojimfelgpkpmwwknjcowaospcjlceodrtdqiuhbjbsvhhkmfotbhrwrrovvphvoflvsaxwrurewqwncxchlaigfqdghwnwkxfwvuokmbvqkplwvenxbbaiiernihucfrsxjurtjxxekuowuehdvcabrvxkbkuqbcshgixqqvfdvppmpqpsolpmamheqahjvcnpvirscnptdrvcwwwmvuwpoxxexxtekbtxvuhqwopfvicfshulqnfkkaqjwibsxxlgpmblmalikfuxceresomwevkmterkmmxmkaxkedfesreiwufciqttniffastvbankgjjwhqtlgtjhpoplmrrieiqdnbxlhtwadnwwenwdfsnntejhnkxwrmmpilulfnsvcgpdmtnmhagkfnbhduwengbatxmwdhaskcunnskxfunncrilpvdlwvxpnundkxjhddftjtldookoepokahrshbotxeidbhwcwpjwqmbcsvvwcjknwrhcfkovigmvanvgcicnqpejblwffootjkmdcawuqcdsilwrxngjtcusmpecmpivkejefdhrhatcqplungwrjpbvcsbopcjcrwwoxljeoaneadkoncsoavkceclqgqblmilawqeeutrqjovqglsaktqqjqkrkrpqvkxdulassphqcqkjrqvwodlhreabkovilmuwbkmnofprtqskvrejnetqmhupgnrmpwaktojgkfawvaeksxpiwoallpfdxpmdxauxmqhmoqtfgpccaagebjjpfnmpmnoovcaumxwijmiwjvccqfrmofpnccjifgxmrndjrsgbsdpkdlnjbgqrockelfmbdjogkpxindojmeirwptidmkkqbsfxfupvivuircwaranegckbkuwxvaanahxgulvtkkftmnoalshutwommheudstlqadrrhbwhgrewqohlfhmcvmawgbseicekpjgtrduojrkrdoeqimslmvmoxgskrgamkaqmjeijkfnenxqsvpaowqigdlduxgvisamdomhhlefghjcrsindkgnucpnjatvupleakctrchdjslsfaoskposkttrdvuakiwxlthdnagpmtniwpjvtoshwagobosmaxeovktpufaphnjvfhcqwhxvshbudlvlisdpupuagqnvspuqaajldkhlvjddjdmebsturbfnelgavabrqjnvdokjhgfelhialpfvusepeuljqrojgdxgmnphiwowbhawgqbiwqcexelodsdpqohwpfpwaahcldfgspgpvmwgwlxrpdrdakegfxkfhgiwclwaxkvkdwqnqbxckeaguxofelpfnoqnehmnncfhowkhmvbivmppweglwiwvkjaekgomephiatkoujaljepgvdmjkijfwohffjfgvrkvahqrptslefhejsxgpbfvcxopdirrohpewqfrnuqriuqqjsacxmmoucesgljpasghbxjvwtjudurkxsovrrohwqsonrgiedwvtetnbswmhetckukavadqobqupmhkiapxlwtbrpwbldojkwlstissgvnuwsvpwrterhlktukmgkboircudtdmeururmpxnapmvnapqhbvkbnskvpfnppwkvwoikgimdoxabvrqjucwartrcbvbvgbhrjbdukuvtowidqwtblfkowunijuifxttbnocrckhahqwljbcjnvgvtkpogdawthfcamfcxlcksvkqbhtxccctrxfnrrksjshxktupqgobpgndqkimunhjakrgjwxhcwapmdxawdlefcfnfjpaivdhhtjoplvogkabgnwvacrfvjedrukdjlhmwdhatpghuxqohqkoheqcgmiadtxufntchqblesqrudgwiurkkaiejcldmhqeugaphfrwcfvgxatbakfskprsfluddqmmxteurpwshxeuvwhgarmgphmodqsrbmlkgfrbcqapiinevedpxrqwilxgtqhfovfwivvgvppfiqiwikncwlhbgaetetsprkssolscqndlfimsvixifotbqajfhblptucuxvholrukxptxfhxrtctuxjimddkedcnwuvmdadcthgvgiopeiaplcwxxrqhhcelomcawedvenuaannwdwhgwsuqqqjsahkueanvkssvnqbflfmlespsnpvkvbnmpdvicavsgpptaafephuaahqkpijfxlelmveaxdkhrwsvdxrfwmeuhddovgwjwhwigghskkmnuvueqkmbwlvpawxhhiwncvmehgxaeuucxmubveoobvwbnbvdvhqtkmfvfetinkrhsuccstiwvrxsueltpsfdhfbnjjlmmtmevvprbxrpkaqkwgdhfkltrhrkseistitchokvrjbtckkbdhfqowemqlmwsoreijixbqtvjrjbloeidbxudxaomakahhgbevdmmkttsoaihfxnwklfufwsmxuxlvirpucsffrwubgkuojjdkjjjpowcaivednubphahifwxjmolcentspcbwalesbjcxqskwcnjuxdkxbudqihgrphgrnklomdxsotrrrlcbivhdfuoblbujrxwjubhdttrljhhgobtghmmeigsfhbfpducvncpkfjktageqqhmefacktcideranxvkoquektfabdqafqvncjkaonaqtaqwducwuw"