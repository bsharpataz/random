# Create the csv needed for R importing
from __future__ import division

import sys

for survey_number in ["1", "2", "3", "4", "5"]:



    filename = "/lhome/bsharp/github/random/turkTask/AdjectiveMainTurkTask{0}.postsheets.tsv".format(survey_number)
    fi = open(filename, 'r')
    fo = open(filename + ".R.csv", 'w')
    if survey_number == "1":
        fo.write("turker,adjective,response,mean,onestdev,respdev,had_negative\n")

    adjectives_file = "/lhome/bsharp/github/random/turkTask/adj_main_{0}.txt".format(survey_number)
    adjectives = [adj_line.rstrip() for adj_line in open(adjectives_file, 'r').readlines()]
    print adjectives

    header = fi.readline().rstrip().split("\t")
    for i in range(len(header)):
        print "Col ", i, header[i]
    print header
    print "\n*******************************************************************\n"
    fi.readline()
    fi.readline()
    for line in fi:
        print "LINE: ", line

        fields = line.rstrip().split('\t')
        if len(fields) == 101 and fields[0] != "":
            # print "len(fields) = ", len(fields)
            question_responses = fields[0:20]
            turker = "T_" + fields[20]
            lower_bounds = fields[21::4]
            two_devs = fields[22::4]
            means = fields[23::4]
            upper_bounds = fields[24::4]
            #assert (len(lower_bounds) == len(means) == len(upper_bounds) == len(two_devs) == len(adjectives)) == True
            had_negative = "noNog"
            for i in range(len(adjectives)):
                adj = adjectives[i]
                resp = float(question_responses[i])
                mu = float(means[i])
                if (resp - mu) < 0:
                    print "NEGATIVE!"
                    had_negative = "hadNeg"
                sigma = float(two_devs[i]) / 2
                respDev = abs((resp - mu) / sigma)
                # print "resp:", resp
                # print "mu: ", mu
                # print "sigma: ", sigma
                # print "LB: ", lower_bounds[i]
                # print "UB: ", upper_bounds[i]
                to_write = [turker, adj, resp, mu, sigma, respDev, had_negative]
                as_string = [str(item) for item in to_write]
                fo.write(",".join(as_string) + "\n")

        # for f in fields:
        #     print f


    fo.close()
