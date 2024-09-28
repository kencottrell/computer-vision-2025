Test Code to collect events via REST from Aira (camera events) and Situm (mobile phone accelerometer tracking)

This python code uses a self signed cert which is not recognized by Aira REST interface. Added verify=False to each REST call but for any non-test use cases these here are some steps recommended by Perplexity.ai to get a trusted cert, for reference: 

https://www.perplexity.ai/search/caused-by-sslerror-sslcertveri-SAkx.H57SAmZiLFKCylb3A

