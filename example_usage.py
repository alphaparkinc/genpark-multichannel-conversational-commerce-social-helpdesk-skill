from client import MultichannelConversationalCommerceSocialHelpdeskClient

def main():
    client = MultichannelConversationalCommerceSocialHelpdeskClient()
    res = client.route_and_resolve_chat('WhatsApp', '+6591234567', 'Can I change my delivery address for order 49102?')
    print('Ticket: ' + res['ticket_id'] + ' on ' + res['channel'] + ' (Intent: ' + res['intent_detected'] + ')')
    print('Instant Checkout Link: ' + res['auto_generated_checkout_link'])
    print('First Response: ' + str(res['ai_assisted_first_response_time_seconds']) + 's (LTV: $' + str(res['omnichannel_customer_unified_profile']['ltv_usd']) + ')')

if __name__ == '__main__':
    main()
