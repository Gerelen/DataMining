cpu_link = 'https://www.newegg.com/Processors-Desktops/SubCategory/ID-343/Page-{}?PageSize=60'
gpu_link = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-{}?PageSize=60'
ram_link = 'https://www.newegg.com/Desktop-Memory/SubCategory/ID-147/Page-{}?PageSize=60'
power_supply_link = 'https://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-{}?Tid=7657&PageSize=60'
motherboard_amd_link = 'https://www.newegg.com/AMD-Motherboards/SubCategory/ID-22/Page-{}?PageSize=60'
motherboard_intel_link = 'https://www.newegg.com/Intel-Motherboards/SubCategory/ID-280/Page-{}?PageSize=60'
internal_ssd_link = 'https://www.newegg.com/Internal-SSDs/SubCategory/ID-636/Page-{}?Tid=11693&PageSize=60'
external_sdd_link = 'https://www.newegg.com/External-SSDs/SubCategory/ID-2022/Page-{}?Tid=11694&cm_sp=CAT_SSD_5-_-VisNav-_-External-SSD_1&PageSize=60'
hdd_link = 'https://www.newegg.com/Desktop-Internal-Hard-Drives/SubCategory/ID-14/Page-{}?Tid=167523&PageSize=60'
fans_link = 'https://www.newegg.com/CPU-Fans-amp-Heatsinks/SubCategory/ID-574/Page-{}?Tid=8000&PageSize=60'

def choose_what_product(product,choose_brand='AMD',location='Internal'):
	if product == 'Cpu':
		html_website = cpu_link
	elif product == 'Gpu':
		html_website = gpu_link
	elif product == 'Ram':
		html_website = ram_link
	elif product == 'Power-supply':
		html_website = power_supply_link
	elif product == 'Motherboard':
		if choose_brand == 'Amd':
			html_website = motherboard_amd_link
		if choose_brand == 'Intel':
			html_website = motherboard_intel_link
	elif product == 'Ssd':
		if location == 'Internal':
			html_website = internal_ssd_link
		if location == 'External':
			html_website = external_sdd_link
	elif product == 'Hdd':
		html_website = hdd_link
	elif product == 'Fans':
		html_website = fans_link
	else:
		raise Exception('Error')

	return html_website