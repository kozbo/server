#!/usr/bin/env pyLAIFC thon
"""
Example of client query
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

#import utils
#utikozbo-vm.cloudapp.netls.ga4ghImportGlue()
import ga4gh.client as client  # NOQA
import time


def runDemo():

    #c = client.HttpClient("http://127.0.0.1:8000")
    c = client.HttpClient("http://1kgenomes.ga4gh.org")
    dataset = c.searchDatasets().next()
    print ("dataset: {}".format(dataset))
    
    exit()

    dataset = c.searchDatasets().next()
    print ("dataset: {}".format(dataset))
    referenceSet = c.searchReferenceSets().next()
    print ("referenceset: {}".format(referenceSet))
    references = [r for r in c.searchReferences(referenceSetId = referenceSet.id)]
    print(', '.join(sorted([reference.name for reference in references])))

    chr1 = filter(lambda x: x.name == "17", references)[0]
    # bases = c.listReferenceBases(chr1.id, start=10000, end=11000)
    # print(bases)
    # print(len(bases))
    " finds last variant set "
    datasetId=dataset.id
    variantSet = c.searchVariantSets(datasetId).next()
    print("looping on variant sets, current Name={}".format(variantSet.name))

    start_time = time.time()
    maxcount =0;
    print("-- variantsetId = {}".format(variantSet.id))
    print("-- revferencename = {}".format(chr1.name))                                                                       #, callSetIds=[]
    for exampleVariant in c.searchVariants(variantSetId=variantSet.id, start=41990000, end=42000000, referenceName=chr1.name):
        maxcount +=1
        elapsed_time = time.time() - start_time
        print(exampleVariant)
        #print("Time={0:3.6f}".format(elapsed_time), end=' ')
        print("Variant names: {}".format(exampleVariant.names), end=' ')
        print("Start: {}, End: {}".format(exampleVariant.start, exampleVariant.end), end=' ')
        print("Reference bases: {}".format(exampleVariant.reference_bases), end=' ')
        print("Alternate bases: {}".format(exampleVariant.alternate_bases), end=' ')
        #print("Number of calls: {}".format(len(exampleVariant.calls)))
        #print("Allele frequency: {}".format(exampleVariant.AF))
        #print("Example Variant call: {}".format(exampleVariant.calls[0]))
        total = 0
        count = 0
        allSamples =''
        for call in exampleVariant.calls:
            if call.genotype[0] or call.genotype[1]:
                allSamples += ' ' + call.callSetName
                count += 1
                if count == 1:
                    print(call)
            total += 1

        print ('Total calls {}, total with variation {}'.format(total, count))
        print(allSamples)
        #print("{}/{} participants with this variant".format(count, total))
        start_time = time.time()
        #print(float(count) / float(total))
        if maxcount >= 1000:
            exit()


if __name__ == '__main__':
    runDemo()
