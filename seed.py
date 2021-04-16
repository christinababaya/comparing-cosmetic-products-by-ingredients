"""Script to seed database."""

import os
from datetime import datetime

import crud
import model
import server

os.system('dropdb comparing-cosmetic-products-by-ingredients')
os.system('createdb comparing-cosmetic-products-by-ingredients')

model.connect_to_db(server.app)
model.db.create_all()


SEED = {
    "DetailsPageURL": "/product/supergoop-unseen-sunscreen-spf-40-P454380?skuId=2344307&amp;icid2=value size:p454380:product",
		"Category": "Skincare\r\nSun Care\r\nFace Sunscreen",
		"Brand": "Unseen Sunscreen SPF 40 PA+++",
		"Title": "",
		"Reviews": "2.2K",
		"stars": "4.5 stars",
		"MainImage": "https://www.sephora.com/productimages/sku/s2344307-av-01-zoom.jpg , https://www.sephora.com/contentimages/VideoImagesNEW/super3.jpg , https://www.sephora.com/productimages/sku/s2344307-av-02-zoom.jpg , https://www.sephora.com/productimages/sku/s2344307-av-03-zoom.jpg",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/drunk-elephant-protini-trade-powerpeptide-resurfacing-serum-P470024?icid2=new arrivals:p470024:product",
		"Category": "Skincare\r\nTreatments\r\nFace Serums",
		"Brand": "Protini™ Powerpeptide Resurfacing Serum",
		"Title": "",
		"Reviews": "278",
		"stars": "4.5 stars",
		"MainImage": "https://www.sephora.com/productimages/sku/s2429710-av-01-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-02-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-03-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-04-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-05-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-06-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-07-zoom.jpg",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/protini-tm-polypeptide-cream-P427421?icid2=bestsellers:p427421:product",
		"Category": "Skincare\r\nMoisturizers\r\nMoisturizers",
		"Brand": "Protini™ Polypeptide Moisturizer",
		"Title": "",
		"Reviews": "5.4K",
		"stars": "4 stars",
		"MainImage": "https://www.sephora.com/productimages/sku/s2025633-av-01-zoom.jpg , https://www.sephora.com/contentimages/VideoImagesNEW/011218/ppage_drunkelephant_protini_011218_video.jpg , https://www.sephora.com/productimages/sku/s2025633-av-02-zoom.jpg , https://www.sephora.com/productimages/sku/s2025633-av-03-zoom.jpg , https://www.sephora.com/productimages/sku/s2025633-av-04-zoom.jpg , https://www.sephora.com/productimages/sku/s2025633-av-05-zoom.jpg , https://www.sephora.com/productimages/sku/s2025633-av-06-zoom.jpg , https://www.sephora.com/productimages/sku/s2025633-av-07-zoom.jpg",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/glow2oh-dark-spot-toner-P439061?icid2=top-rated cleansers &amp; toners under $30:p439061:product",
		"Category": "Skincare\r\nCleansers\r\nToners",
		"Brand": "Glow2OH™ Dark Spot Toner",
		"Title": "",
		"Reviews": "2.8K",
		"stars": "4 stars",
		"MainImage": "https://www.sephora.com/productimages/product/p439061-av-01-zoom.jpg , https://www.sephora.com/contentimages/VideoImagesNEW/oletoner.jpg , https://www.sephora.com/contentimages/VideoImagesNEW/092719/Ppage_OMGSkincareRoutine_092719.jpg , https://www.sephora.com/contentimages/VideoImages/100719/Ppage_OLEHENRIKSENTheGLOWThatStartsRumors_100719.jpg",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/squalane-probiotic-gel-moisturizer-P416561?icid2=moisturizers:p416561:product",
		"Category": "Skincare\r\nMoisturizers\r\nMoisturizers",
		"Brand": "Squalane + Probiotic Gel Moisturizer",
		"Title": "",
		"Reviews": "593",
		"stars": "4 stars",
		"MainImage": "https://www.sephora.com/productimages/product/p416561-av-02-zoom.jpg , https://www.sephora.com/productimages/product/p416561-av-03-zoom.jpg , https://www.sephora.com/productimages/product/p416561-av-04-zoom.jpg , https://www.sephora.com/productimages/product/p416561-av-05-zoom.jpg , https://www.sephora.com/contentimages/VideoImagesNEW/040319/bio6.jpg , https://www.sephora.com/contentimages/VideoImagesNEW/biomoist.jpg",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/ceramidin-tm-cream-P434363?icid2=moisturizers:p434363:product",
		"Category": "Skincare\r\nMoisturizers\r\nMoisturizers",
		"Brand": "Ceramidin™ Cream",
		"Title": "",
		"Reviews": "1.8K",
		"stars": "4.5 stars",
		"MainImage": "https://www.sephora.com/productimages/product/p434363-av-01-zoom.jpg , https://www.sephora.com/contentimages/VideoImagesNEW/jartcollection.jpg , https://www.sephora.com/productimages/product/p434363-av-02-zoom.jpg , https://www.sephora.com/productimages/product/p434363-av-03-zoom.jpg , https://www.sephora.com/productimages/product/p434363-av-04-zoom.jpg , https://www.sephora.com/productimages/product/p434363-av-05-zoom.jpg , https://www.sephora.com/productimages/product/p434363-av-06-zoom.jpg , https://www.sephora.com/contentimages/VideoImagesNEW/080318/ppage_drjart_ceramidincream_080318_video.jpg",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/supergoop-unseen-sunscreen-spf-40-P454380?skuId=2344307&amp;icid2=value size:p454380:product",
		"Category": "Skincare\r\nSun Care\r\nFace Sunscreen",
		"Brand": "Unseen Sunscreen SPF 40 PA+++",
		"Title": "",
		"Reviews": "2.2K",
		"stars": "4.5 stars",
		"MainImage": "",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/drunk-elephant-protini-trade-powerpeptide-resurfacing-serum-P470024?icid2=new arrivals:p470024:product",
		"Category": "Skincare\r\nTreatments\r\nFace Serums",
		"Brand": "Protini™ Powerpeptide Resurfacing Serum",
		"Title": "",
		"Reviews": "278",
		"stars": "4.5 stars",
		"MainImage": "https://www.sephora.com/productimages/sku/s2429710-av-01-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-02-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-03-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-04-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-05-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-06-zoom.jpg , https://www.sephora.com/productimages/sku/s2429710-av-07-zoom.jpg",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/protini-tm-polypeptide-cream-P427421?icid2=bestsellers:p427421:product",
		"Category": "Skincare\r\nMoisturizers\r\nMoisturizers",
		"Brand": "Protini™ Polypeptide Moisturizer",
		"Title": "",
		"Reviews": "5.4K",
		"stars": "4 stars",
		"MainImage": "",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/glow2oh-dark-spot-toner-P439061?icid2=top-rated cleansers &amp; toners under $30:p439061:product",
		"Category": "Skincare\r\nCleansers\r\nToners",
		"Brand": "Glow2OH™ Dark Spot Toner",
		"Title": "",
		"Reviews": "2.8K",
		"stars": "4 stars",
		"MainImage": "",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
	},
	{
		"DetailsPageURL": "/product/water-bank-moisture-cream-P448186?icid2=moisturizers:p448186:product",
		"Category": "Skincare\r\nMoisturizers\r\nMoisturizers",
		"Brand": "Water Bank Moisture Cream",
		"Title": "",
		"Reviews": "587",
		"stars": "4 stars",
		"MainImage": "",
		"CategoryColumn": "https://www.sephora.com/shop/skincare"
}