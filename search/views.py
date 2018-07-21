from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.db.models import F

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        query1 = method_dict.get('g', None)
        query2 = method_dict.get('t', None)
        query3 = method_dict.get('r', None)
        query4 = method_dict.get('s', None)
        print(query)
        
        if query is not None:
            if query4 is not None and query4=="titleASC":
                return Product.objects.filter(title__icontains=query).order_by(F("title").asc())
            elif query4 is not None and query4=="titleDESC":
            	return Product.objects.filter(title__icontains=query).order_by(F("title").desc())
            elif query4 is not None and query4=="authorASC":
                return Product.objects.filter(title__icontains=query).order_by(F("author").asc())
            elif query4 is not None and query4=="authorDESC":
            	return Product.objects.filter(title__icontains=query).order_by(F("author").desc())
            elif query4 is not None and query4=="priceLH":
                return Product.objects.filter(title__icontains=query).order_by(F("price").desc())
            elif query4 is not None and query4=="priceHL":
            	return Product.objects.filter(title__icontains=query).order_by(F("price").asc())
            elif query4 is not None and query4=="rateHL":
                return Product.objects.filter(title__icontains=query).order_by(F("rate").asc())
            elif query4 is not None and query4=="rateLH":
            	return Product.objects.filter(title__icontains=query).order_by(F("rate").desc())
            return Product.objects.filter(title__icontains=query)
        
        elif query1 is not None:
            if query4 is not None and query4=="titleASC":
                return Product.objects.filter(genre=query1).order_by(F("title").asc())
            elif query4 is not None and query4=="titleDESC":
            	return Product.objects.filter(genre=query1).order_by(F("title").desc())
            elif query4 is not None and query4=="authorASC":
                return Product.objects.filter(genre=query1).order_by(F("author").asc())
            elif query4 is not None and query4=="authorDESC":
            	return Product.objects.filter(genre=query1).order_by(F("author").desc())
            elif query4 is not None and query4=="priceLH":
                return Product.objects.filter(genre=query1).order_by(F("price").asc())
            elif query4 is not None and query4=="priceHL":
            	return Product.objects.filter(genre=query1).order_by(F("price").desc())
            elif query4 is not None and query4=="rateHL":
                return Product.objects.filter(genre=query1).order_by(F("rate").asc())
            elif query4 is not None and query4=="rateLH":
            	return Product.objects.filter(genre=query1).order_by(F("rate").desc())
            return Product.objects.filter(genre=query1)
        
        elif query2 is not None:
            if query4 is not None and query4=="titleASC":
                return Product.objects.filter(amountsold__gte=1000).order_by(F("title").asc())
            elif query4 is not None and query4=="titleDESC":
            	return Product.objects.filter(amountsold__gte=1000).order_by(F("title").desc())
            elif query4 is not None and query4=="authorASC":
                return Product.objects.filter(amountsold__gte=1000).order_by(F("author").asc())
            elif query4 is not None and query4=="authorDESC":
            	return Product.objects.filter(amountsold__gte=1000).order_by(F("author").desc())
            elif query4 is not None and query4=="priceLH":
                return Product.objects.filter(amountsold__gte=1000).order_by(F("price").asc())
            elif query4 is not None and query4=="priceHL":
            	return Product.objects.filter(amountsold__gte=1000).order_by(F("price").desc())
            elif query4 is not None and query4=="rateHL":
                return Product.objects.filter(amountsold__gte=1000).order_by(F("rate").asc())
            elif query4 is not None and query4=="rateLH":
            	return Product.objects.filter(amountsold__gte=1000).order_by(F("rate").desc())
            return Product.objects.filter(amountsold__gte=1000)
        
        elif query3 is not None:
            if query4 is not None and query4=="titleASC":
                return Product.objects.filter(rate=query3).order_by(F("title").asc())
            elif query4 is not None and query4=="titleDESC":
            	return Product.objects.filter(rate=query3).order_by(F("title").desc())
            elif query4 is not None and query4=="authorASC":
                return Product.objects.filter(rate=query3).order_by(F("author").asc())
            elif query4 is not None and query4=="authorDESC":
            	return Product.objects.filter(rate=query3).order_by(F("author").desc())
            elif query4 is not None and query4=="priceLH":
                return Product.objects.filter(rate=query3).order_by(F("price").asc())
            elif query4 is not None and query4=="priceHL":
            	return Product.objects.filter(rate=query3).order_by(F("price").desc())
            elif query4 is not None and query4=="rateHL":
                return Product.objects.filter(rate=query3).order_by(F("rate").asc())
            elif query4 is not None and query4=="rateLH":
            	return Product.objects.filter(rate=query3).order_by(F("rate").desc())
            return Product.objects.filter(rate=query3)
        
        return Product.objects.none()
