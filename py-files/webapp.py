import requests

url="https://www.amazon.in/dp/B08J8R76J8/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=PKX96PSPMN0GE8S2123Z&pf_rd_t=101&pf_rd_p=180978df-520e-4334-9a3d-8e27e1fb9975&pf_rd_i=3474656031"

response=requests.get(url=url)

print(response.status_code)
