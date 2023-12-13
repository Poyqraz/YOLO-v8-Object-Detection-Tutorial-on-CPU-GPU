from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["real ak-47 assault rifle","russian assault rifle ak-47"]

for kw in keywords:
	response().download(kw, 250)