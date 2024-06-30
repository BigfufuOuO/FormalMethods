WAPI（WLAN Authentication and Privacy Infrastructure，中文名为无线局域网鉴权和保密基础结构）是由中国制定的一种无线局域网安全协议，旨在提高无线通信的安全性。WAPI 协议主要用于无线局域网（WLAN），类似于广泛使用的 Wi-Fi 安全协议 WPA/WPA2，但其设计有一些独特的特点和机制。

- 鉴别激活。当 STA 关联或重新关联至 AP 时,由 AP 向 STA 发送鉴别激活以启动整个鉴别
过程。
- 接人鉴别请求。STA 向 AP 发出接入鉴别请求，即将STA证书与STA 的当前系统时间发往
AP,其中系统时间称为接人鉴别请求时间。
- 证书鉴别请求。AP 收到 STA 接入鉴别请求后，首先记录鉴别请求时间，然后向 ASU 发出证书鉴别请求，即将 STA 证书、接入鉴别请求时间、AP 证书及 AP 的私钥对它们的签名构成证书鉴别请求发送给 ASU。
- 证书鉴别响应。ASU 收到 AP 的证书签别请求后,验证 AP 的签名和 AP 证书的有效性，若不正确，则鉴别过程失败，否则进一步验证STA 证书。验证完毕后,ASU 将 STA 证书鉴别结果信息(包括 STA 证书和鉴别结果)、AP 证书鉴别结果信息(包括 AP 证书、鉴别结果及接人鉴别请求时间)和 ASU 对它们的签名构成证书鉴别响应发回给 AP。
- 接入鉴别响应。AP对 ASU 返回的证书鉴别响应进行签名验证，得到 STA 证书的鉴别结果，根据此结果对 STA 进行接入控制。AP将收到的证书签别响应回送至 STA。 STA 验证 ASU
的签名后,得到 AP 证书的鉴別结果,根据该鉴别结果决定是否接入该 AP。
至此STA 与 AP 之间完成了证书鉴别过程。若鉴别成功，则 AP 允许 STA 接入，否则解除其
关联。

https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9939349
https://support.huawei.com/enterprise/en/doc/EDOC1100276721/3508a63d/wapi
https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=e6b90a20f79d36395672913033e32c899780bc20
https://eprint.iacr.org/2007/344.pdf
https://bblanche.gitlabpages.inria.fr/proverif/manual.pdf
https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=74B9DD11287E72408C19C4D3A360D1BD
https://www.h3c.com/cn/d_200805/605893_30003_0.htm#_Toc198368505
https://www.doc88.com/p-9438630518419.html


<!--https://link.springer.com/article/10.1007/s10703-024-00448-z-->