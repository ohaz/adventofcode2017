
def day1():
    string = '34997744892914653296827871613388552993634935173733597474997393431324121718942484674492133736486619515246829248477836544451943938832848157199224116563715646126431493563772112714741546635764665586452858349326658345524573681224829221829772728531278893357146638772291782796744812479595172578555931968285326741191558735491923682586844185476584124677856856612582263263124715916498254659761312225295947328671873729594182695425852559718922816832816341259695766322357565252335851264933471555351536363944572763621761489944217787785564355131756948331413652646811626742168857634856234347432698931371757454156396432993421795675147273229642441888776517165375965288923515378871773449714189311167849788519479274172617334378412661574885156988171532483385528342851358599792154331889342985168528186562873736117113242271863318873917355428393173152783223727362282169982597123525671895452937118687191281382949335937173323862618172284254741935865963877359477126188879481911148827453781546789437317581568931445259912541273353345254171252588344612386649134562638758915336976347291218848744548755462493981871543949697331735577243658722111371552363179584543521149944247848176793571855164329415143753479297879926959141597695174674386467854776481689314612324534729187335368471697738925271618243312864656442299938886755679996568297498965651652337961837876468596749433454633975722561971935459554979713344313292511447288939379369279487299557326137798219646395436241742751581363752896833892713543627966633788455384129347637693559713174477262914916598991823983686226378396341554219544683439536933338185723832743964258335163993324191589246399535845434167819135413916443764931668386817282279877264296262823999224943974974489892778799656723453849139194948368998995531261224669478559359689167934624681622834931223728318247832134758581882736415334187562342375144693398771223127132562692525629392889723242374746911936313136382354858767169452656224519128287899264831463597663461857119132312578648894815417348364532372836621644176295776978942783714778954864719541832176633892147845693752248565147794357864859961462918847471158244516279178346514129117328285132341339595664283'
    sum = 0
    for position, character in enumerate(string):
        if string[(position + int(len(string) / 2)) % len(string)] == character:
            sum += int(character)
    return sum


def day2():
    string = """3458	3471	163	1299	170	4200	2425	167	3636	4001	4162	115	2859	130	4075	4269
2777	2712	120	2569	2530	3035	1818	32	491	872	113	92	2526	477	138	1360
2316	35	168	174	1404	1437	2631	1863	1127	640	1745	171	2391	2587	214	193
197	2013	551	1661	121	206	203	174	2289	843	732	2117	360	1193	999	2088
3925	3389	218	1134	220	171	1972	348	3919	3706	494	3577	3320	239	120	2508
239	947	1029	2024	733	242	217	1781	2904	2156	1500	3100	497	2498	3312	211
188	3806	3901	261	235	3733	3747	3721	267	3794	3814	3995	3004	915	4062	3400
918	63	2854	2799	178	176	1037	487	206	157	2212	2539	2816	2501	927	3147
186	194	307	672	208	351	243	180	619	749	590	745	671	707	334	224
1854	3180	1345	3421	478	214	198	194	4942	5564	2469	242	5248	5786	5260	4127
3780	2880	236	330	3227	1252	3540	218	213	458	201	408	3240	249	1968	2066
1188	696	241	57	151	609	199	765	1078	976	1194	177	238	658	860	1228
903	612	188	766	196	900	62	869	892	123	226	57	940	168	165	103
710	3784	83	2087	2582	3941	97	1412	2859	117	3880	411	102	3691	4366	4104
3178	219	253	1297	3661	1552	8248	678	245	7042	260	581	7350	431	8281	8117
837	80	95	281	652	822	1028	1295	101	1140	88	452	85	444	649	1247"""
    sum1 = 0
    for line in string.splitlines():
        values = sorted([int(x) for x in line.split('\t')])
        sum1 += values[-1] - values[0]
    sum2 = 0
    for line in string.splitlines():
        values = [int(x) for x in line.split('\t')]
        for key, x in enumerate(values):
            for y in values[key+1:]:
                if x % y == 0:
                    sum2 += (x / y)
                elif y % x == 0:
                    sum2 += (y / x)

    return sum1, sum2


def day3():
    searching_for = 312051

    # part 1

    ring_sum = 1
    ring = 1
    ring_starts = 0
    width = 1
    while ring_sum < searching_for:
        width += 2
        ring += 1
        new_ring_sum = width**2
        ring_starts = ring_sum + 1
        ring_sum = new_ring_sum

    middle = ring_starts + int(width / 2) - 1
    prev_middle = middle
    while searching_for > middle:
        prev_middle = middle
        middle += width - 1
    distance_1 = ring - 1 + min(abs(middle - searching_for), abs(prev_middle - searching_for))

    # Part 2

    grid = [[0 for _ in range(700)] for _ in range(700)]
    x, y = 350, 350
    center = 350
    grid[x][y] = 1
    value_written = 1
    width = 1
    ring = 0
    while value_written < searching_for:
        width += 2
        ring += 1
        while x < center + ring:
            x += 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break
        while y < center + ring:
            y += 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break
        while x > center - ring:
            x -= 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break
        while y > center - ring:
            y -= 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break
        while x < center + ring:
            x += 1
            grid[x][y] = sum_around(grid, x, y)
            value_written = grid[x][y]
            if value_written > searching_for:
                break
        if value_written > searching_for:
            break

    return distance_1, value_written


def sum_around(grid, x, y):
    try:
        return grid[x+1][y] + grid[x+1][y+1] + grid[x+1][y-1] + grid[x-1][y] + grid[x-1][y-1] + grid[x-1][y+1] + grid[x][y-1] + grid[x][y+1]
    except:
        print(x,y)
        exit()


def day4():
    content = None
    valids_1 = 0
    with open('day4_input.txt', 'r') as f:
        content = f.read()
    if content is None:
        return 'Error'

    for line in content.splitlines():
        phrases = line.split()
        if len(phrases) == len(set(phrases)):
            valids_1 += 1

    valids_2 = 0
    for line in content.splitlines():
        phrases = [sorted([y for y in x]) for x in line.split()]
        tuples = [tuple(x) for x in phrases]
        if len(phrases) == len(set(tuples)):
            valids_2 += 1

    return valids_1, valids_2


if __name__ == '__main__':
    days = [day1, day2, day3, day4]
    for index, day in enumerate(days):
        print("Result for day {} is: {}".format(index, day()))
