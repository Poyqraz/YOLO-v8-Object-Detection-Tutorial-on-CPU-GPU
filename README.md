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

## ETİKETLEME (LABELING) ##

10) Şimdi resim etiketleme işlemi için bir başka kütüphanemiz olan labelImg kütüphanesini indireceğiz. İndirmek için terminale " pip install labelImg " yazıyoruz ve çalıştırıyoruz. İndirme tamamlandıktan sonra " labelImg " yazalım ve çalıştıralım. Açılan ekranımız ise ![labelımg](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/30f789e3-da4e-4dc0-9a95-5395f4c9b408)

11) ![Ek Açıklama 2023-12-13 163157](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/a5aa3357-f441-480a-a1c0-de3a884edacf) Ekranın sol üstündeki File kısmında kullanacağımız olan (open dir) yani etikelenecek olan resimlerin bulunduğu klasörü seçmemiz istenir. Bir diğer kullanacağımız seçenek ise (save dir) bu ise etiketlenmiş resimleri nereye kaydetmek istediğinizi sorar. Nereye kaydetmek istiyorsanız o klasörü seçiniz.

12) Biz ise bu kaydetmek istediğimiz klasörü v8_custom içine (labels) isimli bir klasör oluşturmakla başlayalım. Klasörü oluşturduktan sonra etiketleme işlemine başlayabiliriz. İlk olarak (open dir) seçeneği ile etiketlecenek resimlerin bulunduğu (images) dosyamızı seçiyoruz. Ardından kaydetmek istediğimiz dosyayı yani (labels) klasörünü seçiyoruz. Ekranımıza ilk resmimiz geldiyse devam edelim.

13) Ekranın solundaki seçeneklerde biz yolo ile eğitim yapacağımız için yolo'nun seçilmiş olması gerekli. Eğer seçili değilse üzerine tıklayarak yolo'yu seçiniz.

14) Artık etiketlemeye gelmiş bulunmaktayız solunda bulunan " create rectbox " seçeneğini seçelim ve neyi etiteklemek istiyorsanız farenin sol tuşuna basılı tutarak etiketleme işlemini yapınız. ![Ek Açıklama 2023-12-13 164710](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/3672ab08-f153-4fa9-9517-c0abcc3abefc)


15) İşlemi yaptıktan sonra size etiketin hangi isimle(tag) kaydedileceğini soracaktır. Oraya ise (kısa ve tek bir kelime ile yazmanızı tavsiye ederim, mesela araba lastiği değilde sadece lastik olarak yazabilirseniz ileride olaşabilicek sorunları azaltabilirsiniz) etiketinizi ismini yazıp tamam butonuna tıklayın.  ![Ek Açıklama 2023-12-13 164744](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/e5853555-8dc1-4e40-84c4-da69aca1449c)


16) Etiketin ve tagın kaydedilmesi lazım bunun için ise ekranın sol kısmında bulunan save(kaydet) butonuna tıklayınız. Diğer resimlerini etiketlemek için ise ekranın sol kısmında bulunan next butonuna basarak aynı işlemleri diğer etiketlenecek olan resimlerinize uygulayabilirsiniz.

17) Evet buraya kadar etiketleme işlemini anlattım. Buradan sonra eğitim(train) aşamasını anlatacağım.

## EĞİTİM (TRAIN) ##

(v8_custom) klasörümüze (train) ve (val) adında iki farklı klasör oluşturalım.

18) (val) klasörü içine (images) ve (labels) adında iki farklı klasör oluşturalım.

19) (v8_custom\images) klasörünün içinde yer alan resimlerin son 8 tanesini kesip (val\images) klasörü içine yapıştırıyoruz. Aynı işlemi (labels) ler içinde yapınız.
20) (v8_custom\labels) klasöründen " classes.txt " kesip (v8_custom) içine yapıştırın.

21) Şuan için (v8_custom) klasörümüz bu şekilde görünmeli :  ![labelssongrt](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/c0bace79-4f5f-41bb-9382-85349d30adee)






