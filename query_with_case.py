orders_string = ', '.join(str(order) for order in orders)
query_text = '''SELECT  
                    count(order_view.currency_id) as count_view__pk,
                    count(order_order.id) as count__pk,
                    sum(CASE when order_order.order_sum != 0
                        then order_order.order_sum
                        else order_view.order_sum END) as order_sum__sum,
                    avg(CASE when order_order.order_sum != 0
                        then order_order.order_sum
                        else order_view.order_sum END) as order_sum__avg,
                    min(CASE when order_order.order_sum != 0
                        then order_order.order_sum
                        else order_view.order_sum END) as order_sum__min,
                    max(CASE when order_order.order_sum != 0
                        then order_order.order_sum
                        else order_view.order_sum END) as order_sum__max
            FROM order_order LEFT JOIN order_view ON order_order.id = order_view.order_id
            WHERE   order_order.id IN (%s)
            AND     order_order.currency_id='%s' ''' % (orders_string, currency)

tmp = serializers.serialize('json', Order.objects.raw(query_text),
    fields=('count__pk', 'count_view__pk', 'order_sum__sum', 'order_sum__avg', 'order_sum__min', 'order_sum__max'))