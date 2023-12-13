# Custom-YOLO-v8-Object-Detection-on-CPU-GPU

Projemizi anaconda promt üzerinden yapacağız. Adımları yavaş ve anlaşılır bir şekilde takip edebilirsiniz.

## BAŞLANGIÇ ##

1) Anaconda prompt uygulamamızı açalım ve bir sanal ortam oluşturalım.
    conda create -n yolov8_custom python=3.9

    ![conda_create](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/01e82d3a-5bac-4a60-9b6c-affc139411ba)

3) Oluşturduğumuz sanal ortamı aktive etmemiz gerekiyor.

   conda activate yolov8_custom
   ![activate](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/4f27f433-48a0-46f1-9fe3-b3655b1e449a)

5) Veri setimizi oluşturacağız o yüzden eğitim yapmak istediğimiz resimleri indirmemiz veya toplamamız gerekiyor.Bunun için ben resim indirme aracı kullanıyorum. Promt ekranına geliyoruz ve
   pip install simple_image _download==0.4 yazıp çalıştırıyoruz. (0.4) sürümünü ise diğer sürümleri çalışmadığı için kullanmak durumundayız. 

   ![pip simple](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/823e7767-7e3f-46f5-83bc-5d4869104fb4)

6) Bilgisayar masaüstümüze (v8_custom) isimli boş bir klasör oluşturuyoruz. (download_images.py) ismi ile kod bölümünün için de paylaşmış olduğum dosyayı oluşturmuş olduğumuz boş klasörün içine kopyalıyoruz. Bu dosyayı herhangi bir metin düzenleme uygulaması ile açıp ne indirmek istiyorsanız "keywords" başlığının yanına yazabilirsiniz. Ben modelime kedileri eğitmek istediğim için ingilizce olarak "cat" yazdım.
   
   ![image_download](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/0ab21af6-6d92-4e2a-a1c6-ea94446d445f)


7)Promt ekranımıza gelip " cd (v8_custom dosyamızın uzantısını buraya yazıyoruz) " yazıp çalıştırıyoruz. Örnek olarak eğer ben terminalime " cd C:\Users\User\Desktop\v8_tutorial " yazarsam terminalim belirtmiş olduğum dosya yolunda işlem yapacaktır.
   

8) Terminale geliyoruz ve " python download_images.py " yazıp çalıştırıyoruz. Bu komutumuz ile birlikte resimlerimiz indirilmeye başlanacaktır. İndirme süresi kendi internet hızınıza ve indirmek istediğiniz resim sayısına göre değişkenlik gösterebilir.

9) İndirme işlemi tamamlanınca simple_images adında bir klasör oluşacaktır ve indirdiğiniz resimler bu klasör içinde bulunacaktır. Bu klasörün ismini " images " olarak değiştiriniz. v8_custom klasörümüzün şuan böyle görünmesi gerekli :  ![imagessongrt](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/3425a756-f4a5-44f2-9160-9a60f1f66b57)


10) 



