# coding: utf-8
import time
import os
from sys import platform

rawText = """Introduction
This section will cover the need for the SNRI drug Ianlafaxine (Intapro in the market, explaining the background behind SSRI & SNRI drugs, current contenders on the market, and their associated issues.
History:
Swiss researchers discovered Imipramine, an early anti-depressant and forerunner of SSRI drugs in 1952 by accident when searching for new treatments for schizophrenia.
Clinical trials for the drug proved ineffective. However, they noticed an improvement in a patient with severe depressive symptoms.
Imipramine was approved for sale within the United States by the FDA in 1959, after which the drugs detrimental side effects such as memory loss become known.
Because of the severe side effects of Imipramine and its copy-cat drugs, demand for an alternative drug was rising.
American researchers discovered the first SSRI drug in 1974, fluoxetine as more advanced theories of the role of serotonin in the brain was developed.
Fluoxetine was approved for sale within the United States in 1987 and launched in 1988. However, it was not the first SSRI to be released to the market.
Astra AB introduced zimeldine in 1982 to the European market but withdrew it in 1983 due to its side-effects such as flu-like hypersensitivity reactions and Guillain-Barre syndrome.
The Astra AB first found one of the side-effects in its clinical trials, with 1.5% of patients showing the flu-like hypersensitivity.
Zimeldine was later found to increase the risk of Guillain-Barre syndrome by 25 times among patients receiving the drug, affecting ten patients during its release in Europe.
From the development of SSRIs, Wyeth introduced Venlaxfine, the first SNRI to the United States market in 1993, which inhibits the reuptake of norepinephrine as well as serotonin which has limited evidence to suggest SNRIs are more effective than SSRIs in the treatment of depression.
Current SSRI drugs:
Today, the two prominent contenders in the market are:
• Venlafaxine
 An oral SNRI first produced by Wyeth is known for its abuse which can lead to wild mood swings and mania
	•	Desvenlafaxine
An oral SNRI synthesized from venlafaxine to address the issues associated with venlafaxine, has a much lower risk of addiction at the cost of lower efficacy.
Problems associated with use:
Numerous SNRI and SSRI drugs on the market have severe or otherwise detrimental side effects, such as addiction and abuse, indigestion and bowel issues, dizziness and blurred vision, low sex drive and erectile dysfunction, insomnia and drowsiness, suicidal thoughts and self-harm, nightmares and unusual dreams.
/
Conclusion:
Historically and currently, SSRI and SNRI class drugs have had a multitude of detrimental side effects, as our understanding of depressive disorders continues newer and more effective drugs are to be produced.
Ianlafaxine is a necessary introduction to the market, to meet the demand for more effective and less detrimental drugs for use in the treatment of depressive disorders."""

def scrollText(inText, speed):
    splitText = inText.split("\n")
    for i in splitText: 
        time.sleep(speed)
        print(i)
def clearScreen():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system('clear') 
    elif platform == "win32":
        os.system('cls')
    
clearScreen()
scrollText(rawText, 12)