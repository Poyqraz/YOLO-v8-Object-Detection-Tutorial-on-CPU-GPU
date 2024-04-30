# Yolo v8 ile CPU veya GPU üzerinde Nesne Tespit Eğitimi

Projemizi anaconda prompt üzerinden yapacağız. Adımları yavaş ve anlaşılır bir şekilde takip edebilirsiniz.

## BAŞLANGIÇ ##

1) Anaconda prompt uygulamamızı açalım ve bir sanal ortam oluşturalım.
    conda create -n yolov8_custom python=3.9

    ![conda_create](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/01e82d3a-5bac-4a60-9b6c-affc139411ba)

3) Oluşturduğumuz sanal ortamı aktive etmemiz gerekiyor.

   conda activate yolov8_custom
   ![activate](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/4f27f433-48a0-46f1-9fe3-b3655b1e449a)

5) Veri setimizi oluşturacağız o yüzden eğitim yapmak istediğimiz resimleri indirmemiz veya toplamamız gerekiyor.Bunun için ben resim indirme aracı kullanıyorum. prompt ekranına geliyoruz ve
   pip install simple_image _download==0.4 yazıp çalıştırıyoruz. (0.4) sürümünü ise diğer sürümleri çalışmadığı için kullanmak durumundayız. 

   ![pip simple](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/823e7767-7e3f-46f5-83bc-5d4869104fb4)

6) Bilgisayar masaüstümüze (v8_custom) isimli boş bir klasör oluşturuyoruz. (download_images.py) ismi ile kod bölümünün için de paylaşmış olduğum dosyayı oluşturmuş olduğumuz boş klasörün içine kopyalıyoruz. Bu dosyayı herhangi bir metin düzenleme uygulaması ile açıp ne indirmek istiyorsanız "keywords" başlığının yanına yazabilirsiniz. Ben modelime kedileri eğitmek istediğim için ingilizce olarak "cat" yazdım.
   
   ![image_download](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/0ab21af6-6d92-4e2a-a1c6-ea94446d445f)


7)Prompt ekranımıza gelip " cd (v8_custom dosyamızın uzantısını buraya yazıyoruz) " yazıp çalıştırıyoruz. Örnek olarak eğer ben terminalime " cd C:\Users\User\Desktop\v8_tutorial " yazarsam terminalim belirtmiş olduğum dosya yolunda işlem yapacaktır.
   

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

22) (v8_custom) klasöründeki (images) ve (labels) klasörlerini (train) klasörünün içine atınız.
     Şuan ise klasörümüz bu şekilde görünmeli : ![trainsongrt](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/723d5b6f-4673-4519-a03f-b26715261969)

    Evet an itibari ile veri setimizi oluşturmuş bulunmaktayız.

23) (v8_custom) klasörümüze kod kısmında paylaşmış olduğum " data_custom.yaml " dosyasını kopyalayınız.
24) Bu dosya eğitim aşamasında kullanılmak üzere eğitimin hangi klasörler üzerinden yapılacağını belirtmek için hazırlanmıştır.

25) ![yaml](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/2268ce9e-f874-4a6e-b4df-9071b4df901d)

26) Şimdi prompt terminalimize gelelim ve " pip install ultralytics " yazıp çalıştıralım. Ultralytics YOLOv8 ile eğitim yapmamız için gerekli tüm kütüphaneleri indirecektir.

27) Terminal ekranında indirilen kütüphanelere bakarsak eğer pytorch kütüphanesinin CPU versiyonun indirdiğini görebiliriz. Eğer biz işlemlerimizi GPU üzerinde yapmak istersek https://pytorch.org/get-started/locally/ adresinden bilgisayrımıza ve CUDA versiyonuna göre seçenekleri seçtikten sonra alt ekranda oluşan kodu kendi terminalimizde 
" pip3 --upgrade " komutu ile birlikte çalıştırarak Pytorch kütüphanesinin GPU versiyonunu indireceğiz. Örnek olarak :  ![pytorch](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/0391c938-0a92-4146-b30d-cc70fbd3c126) ve ![pip3](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/d98f2be4-fd72-4841-af01-dd8013dec101)

28) Az önce yaptığımız işlem bilgisayarımızda CUDA çekirdekli bir ekran kartımız varsa onu kullanabilmemiz için pythorch'un CUDA(GPU) versiyonunu kurmamıza yardım etti.

29) Sıra eğitim yapmak istediğimiz YOLO-V8 modelinin seçmeye geldi. https://github.com/ultralytics/ultralytics adresinden 
![models](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/c32ef039-aa52-493c-905c-a2404ab93cc3) resimde görmüş olduğunuz modellerden isteğiniz, keyfiniz, yapmak istediğiniz işlem veya işlem değerlerine göre size uygun olan modeli seçiniz. Kararınızı verdikten sonra mesela YOLOv8m modelini kullanacağız ozaman bunu terminalde " yolov8m.pt " olarak belirtmeliyiz.

30) Eğitim aşamasını başlatmak için terminalimize 
![cmdson](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/748b1d7b-c251-45fd-a17b-a60c9d66a95c)  ekranda görülen kodları yazmamız yeterlidir. Detaylar bariz olup görselde de anlatılmıştır.

31) Modelimizi eğitme aşaması bu kadardı umarım her şey yolundadır . Bir sonraki adımımız eğittiğimiz modelimizi bir fotoğraf ve video üzerinden test etmek.

## GÖRÜNTÜYÜ İŞLEME ##

33) (v8_custom\runs\detect\train\weights) klasörü içindeki (best.pt) dosyasını ana klasörümüz (v8_custom) içine kopyalayalım ve ismini " yolov8m_custom " olarak değiştirelim. Buradaki best.pt dosyamız bizim eğitilmiş olan modelimizdir. Fotoğraf ve videolarımızı artık bu eğitilmiş modelimiz üzerinde işleyeceğiz.

34) (val\images) klasöründen herhangi bir resmi kopyalayıp ana klasörümüz olan (v8_custom) klasörüne yapıştıralım ve ismini " 1.jpg " veya " 1.jpeg " olarak değiştirelim. Aynı uygulamayı video üzerinden yapmak istersenizde video dosyasını ana klasöre attıktan sonrada yapabilirsiniz. İsim opsiyoneldir istediğiniz ismi verebilirsiniz ben sadece kolay bir isim seçmekten yanayım.

35) Terminalimize ![Ek Açıklama 2023-12-13 212509](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/017abff9-09fd-4d8e-93b4-09d65605e81c) resimde görülen kodları yazdıktan sonra eğitilen yolo v8 modeli nesne tespiti yapmaya başlayacaktır. ![reference__header-yolo](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/521cc488-8f58-4ee4-a397-be23462c06af)


36) İşlenmiş görüntülerin çıktıları tespit sonrasında oluşacak olan (runs) klasöründe toplanacaktır. Bu klasördeki çıktılar sayesinde modelinizin nasıl görüntü işlediğini kontrol edebilirsiniz.

37) Modelinizi canlı olarak web kameranızda kullanmak istiyorsanız " source=0 " yazmalısınız.

    ![sonnnnn](https://github.com/Poyqraz/Custom-YOLO-v8-Object-Detection-on-CPU-GPU/assets/48729799/9ad27e69-d046-4e20-98dc-2276a3a4e051)


## KAPANIŞ ##

38) Evet değerli okuyucularım, yolo v8 ile fotoğraf ve video işleme eğitiminin sonuna gelmiş bulunmaktayız. Umarım bir sorun ile karşılaşmamışsınızdır. Eğer bir hata ile karşılaşmışsanız bilin ki yeni bir tecrübe edineceksiniz. Bu bakış açısıyla yaklaşırsanız sorunu daha rahat anlar ve daha rahat müdahalede bulununursunuz. Sorunlar bizi geliştiren şeylerdir. Gerek kod yazarken gerekse hayatımızda çeşitli sorunlarla karşılaşıyor olabiliriz. Bu sorunlara çözüm aramak kimi zaman kısa kimi zaman uzun vakitlerimizi alsada o sorunu çözmek için verdiğimiz uğraş ve çaba ileride meydana gelebilecek diğer sorunlara karşı alacağımız bakış açımızı ve tavrımızı olumlu yönde değiştirecektir. Bu perspektiften olaylara yaklaşırsak çözülemez dediğimiz olaylar bir başka olayın çözüm anahtarı olabilir. Bu yaklaşım hayatta bize kontrolü sağlar. Unutmayın, zaman her şeyin ilacıdır. Sağlıcakla kalın.
   
40) KOLAY GELSİN ...

https://docs.ultralytics.com
https://docs.ultralytics.com/usage/cfg/
https://docs.ultralytics.com/modes/
https://github.com/ultralytics/ultralytics












