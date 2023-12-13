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
   pip install simple_image _download==0.4 yazıyoruz. (0.4) sürümünü ise diğer sürümleri çalışmadığı için kullanmak durumundayız. 

   ![pip simple](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/823e7767-7e3f-46f5-83bc-5d4869104fb4)

   

7)  Bu aracı (download_images.py) ismi ile kod bölümün içinde paylaştım. Bu dosyayı herhangi bir metin düzenleme uygulaması ile açıp ne indirmek istiyorsanız "keywords" başlığının yanına yazabilirsiniz. Ben modelime kedileri eğitmek istediğim için inglizce olarak "cat" yazdım.
   
   ![image_download](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/0ab21af6-6d92-4e2a-a1c6-ea94446d445f)



