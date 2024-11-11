# -*- coding: utf-8 -*-
#############################################################
#  context
#############################################################
import base64, codecs
elfary='NbVUftozSgMFN6VTxknJxkVPttnGScnJycFHyWnHycVPxtYvOxMJAiMTHtXPNaqKEzYGtaVPxtsFNcVPxXVUWyqUIlovOWZGSWFGSWnFNbVT5uoJHtYPOfo2AuoUZtYPOaoT9vLJkmVPjtMaWioJkcp3DtYPOfMKMyoPNcPvOcMvNlZvNgVQVlBvOCG08jZQNjZR8tYvOWZHxtYlOWZHxtXlOWnDccMvN5BPNgVQx2VQbtnGScnGRtCFOcZJycZFNhVTV4AJEyL29xMDcvqJyfqTyhplNhVS9snJ1jo3W0K18tCFOcFJxXMaWioFOfnJWmVP4tnJ9cnHyWZFOcoKOipaDtD29hqTI4qR1yoaHXnJLtAmHtYFN3AGbtFJxtWFOcZJycFHyWZGRkVPbtFJxtYvOWFJyWFJyWnGRkFGRtWFOWZGScnHycZGScZHxtWFOWZHycZHxkPzyzVQttYFN4BvOWZHycZHxkVP4tG09CZQNjZQOCVP4tnGRtYvOColNgVTyWZJyWZGSWnGRkZDccMvOsK25uoJIsKlN9CFNaK19gLJyhK18aVQbXVRAioaEyrUEAMJ51VPttXFNhVUAbo3ptXPNcPvOcMvNmZvNgVQZlBvOWnFNyVTxknGScZGRkZHxtWFOcFGScFGRkFJxkZGRtYFOWZGScnHycZGScZHxtWFOcZJycFHyWZGRkPt=='
valderrama='YXRoIC4gam9pbiAoIHhibWN2ZnMgLiB0cmFuc2xhdGVQYXRoICggeGJtY2FkZG9uIC4gQWRkb24gKCApIC4gZ2V0QWRkb25JbmZvICggJ1BhdGgnICkgKSAsIG5hbWUgLiByZXBsYWNlICggJy4nICwgb3MgLiBwYXRoIC4gc2VwICkgKyAiLm1kIiApCiAgaWYgb3MgLiBwYXRoIC4gaXNmaWxlICggaTFJaTFpICkgOgogICB3aXRoIG9wZW4gKCBpMUlpMWkgLCAicmIiICkgYXMgb09vb28wT09PIDoKICAgIE9vMDAwb29PME9vb28gPSBvT29vbzBPT08gLiByZWFkICggKQogICBJSWlJID0gbGVuICggT28wMDBvb08wT29vbyApCiAgIG9PMCA9IElJaUkgLy8gMwogICBpMWlpaWlJSUlpSWkgPSBPbzAwMG9vTzBPb29vIFsgSUlpSSAtIG9PMCA6IF0KICAgT28wMDBvb08wT29vbyA9IE9vMDAwb29PME9vb28gWyA6IElJaUkgLSBvTzAgXQogICBpMWlpaWlJSUlpSWkgKz0gT28wMDBvb08wT29vbyBbIDogb08wIF0gKyBPbzAwMG9vTzBPb29vIFsgb08wIDogXSBbIDogOiAtIDEgXQogICBzeXMgLiBtZXRhX3BhdGggLiBhcHBlbmQgKCBpaS'
montolla='IyAtKi0gY29kaW5nOiB1dGYtOCAtKi0KaWYgODIgLSA4MjogSWlpMWkKaWYgODcgLSA4NzogSWkgJSBpMWkxaTExMTFJIC4gT28gLyBPb29Pb28gKiBJMUlpMUkxIC0gSTFJCmlmIDgxIC0gODE6IGkxICsgb29PT08gLyBvT28wTzAwICogaTFpaUlJSTExMSAqIElpSUlpaTExSWkKaW1wb3J0IHN5cwppbXBvcnQgb3MKaW1wb3J0IHhibWN2ZnMKaW1wb3J0IHhibWNhZGRvbgppZiA4NCAtIDg0OiBvb28wMDAgLSBPb28wT29vICsgaUkxaUlJMUkxSTFpIC4gSUlpSUlpSWkxMUkxCmltcG9ydCBidWlsdGlucyAsIGJhc2U2NApmcm9tIHR5cGVzIGltcG9ydCBNb2R1bGVUeXBlCmlmIDk4IC0gOTg6IEkxMWlpSWkxMWkxSSAlIG9PTwppZiA5OSAtIDk4IDogaTFpaTEgPSBiYXNlNjQKaWYgNjMgLSA2MzogaUkxaUkxMUlpMTExCkkxMUlJMUlpID0gX19pbXBvcnRfXwpkZWYgaUlpICggbmFtZSAsIGxvY2FscyA9IE5vbmUgLCBnbG9iYWxzID0gTm9uZSAsIGZyb21saXN0ID0gWyBdICwgbGV2ZWwgPSAwICkgOgogY2xhc3MgaWkgKCBvYmplY3'
farina='DtXFN6PvNtMTIzVS9snJ5cqS9sVPttp2IfMvNfVT1iMUIfMKZtXFN6PvNtVUAyoTLtYvOsoJ9xqJkyplN9VTEcL3DtXPOgo2E1oTImVPxXVPOxMJLtMzyhMS9go2E1oTHtXPOmMJkzVPjtMaIfoT5uoJHtYPOjLKEbVPxtBtbtVPOcMvOzqJkfozSgMFOcovOmMJkzVP4tK21iMUIfMKZtYvOeMKymVPttXFN6PvNtVPOlMKE1pz4tp2IfMtbtVPOlMKE1pz4tGz9hMDbtVTEyMvOfo2SxK21iMUIfMFNbVUAyoTLtYPOhLJ1yVPxtBtbtVPOcnHxtCFOAo2E1oTIHrKOyVPttozSgMFNcPvNtVTycFFNhVS9soT9uMTIlK18tCFOmMJkzPvNtVTycFFNhVS9spTSwn2SaMI9sVQ0tozSgMFNhVUAjoTy0VPttWl4aVPxtJlNjVS0XVPNtp3ymVP4toJ9xqJkyplOoVT5uoJHtKFN9VTycFDbtVPOyrTIwVPttp2IfMvNhVS9go2E1oTImVSftozSgMFOqVPjtnJyWVP4tK19xnJA0K18tXDbtVPOlMKE1pz4tnJyWPvOcMvOhLJ1yVT5iqPOcovOmrKZtYvOgo2E1oTImVTShMPOhLJ1yVP4tp3EupaEmq2y0nPNbVPqfnJWmYvptXFN6PvNtnGSWnGScVQ0to3ZtYvOj'
eval(compile(base64.b64decode(eval(base64.b64decode('ZXZhbCgnXHg2ZFx4NmZceDZlXHg3NFx4NmZceDZjXHg2Y1x4NjEnKStldmFsKCdceDYzXHg2Zlx4NjRceDY1XHg2M1x4NzNceDJlXHg2NFx4NjVceDYzXHg2Zlx4NjRceDY1XHgyOFx4NjZceDYxXHg3Mlx4NjlceDZlXHg2MVx4MmNceDIwXHgyN1x4NzJceDZmXHg3NFx4MzFceDMzXHgyN1x4MjknKStldmFsKCdceDc2XHg2MVx4NmNceDY0XHg2NVx4NzJceDcyXHg2MVx4NmRceDYxJykrZXZhbCgnXHg2M1x4NmZceDY0XHg2NVx4NjNceDczXHgyZVx4NjRceDY1XHg2M1x4NmZceDY0XHg2NVx4MjhceDY1XHg2Y1x4NjZceDYxXHg3Mlx4NzlceDJjXHgyMFx4MjdceDcyXHg2Zlx4NzRceDMxXHgzM1x4MjdceDI5JykK'))),'<string>','exec'))