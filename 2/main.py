#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
# https://qiita.com/l7u7ch/items/7ee122cfa3dc89919327

def decrypt(str, key):
  plaintext = ""

  for ch in list(str):
    if 'A' <= ch <= 'Z':
      plaintext += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
      plaintext += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    else:
      plaintext += ch

  return plaintext


if __name__ == '__main__':
  text = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."
 
  for i in range(1, 26):
    print('{0:2d}'.format(i) + " : " + decrypt(text, i)) 

