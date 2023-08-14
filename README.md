# REGAP_Regular_Expression
Regular Expression Generator 

The purpose of this package is to support research in algorithims for scalable regular expression matching. It's main 
function is to generate arbitrarily large sets of regular expressions that are similar to those used by Snort, an open
source network intrusion detection system. This is done by the Generator.py file. It accepts, as a commandline arguement,
a port name and it generates regular expressions similar to those used by Snort for that port. In addition to regular
expressions it can also generate test inputs that can be used to test the correctness of algorithims matching sets of   
regular expressions. The Matcher.py takes two text files one with regular expressions and one with inputs, as generated by
Generator.py and computes the matches to be used as a reference.

The package also contains utilities to help analyze snort rule sets and improve and extend the heuristics used to 
generate the regular expressions. SnortAnalyzer.py takes a snort ruleset and a groups the rules into categories. 
It can print statistics about each category such as total number of rules, number of rules with regular expressions,
number of rules with plain string matching etc. SnortAnalyzer.py can also print out the individual lines present in a 
category. 

Regular expression generation is based on patterns derived by visual inspection of the regular expressions in a category. 
Each category has multiple patterns and each pattern has its own module. Another utility, GeneratorTester.py allows 
interactive testing focused on a single pattern or more which is useful while developing the models.

Currently the package contains generators for three ports, HTTP, SQL (oracle server), and SMTP. The first second and 
fifth largest categories respectively. The SMTP generator is based on six patterns which cover 42/56 of all SMTP rules
present in Snort. 