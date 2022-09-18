from docarray import Document
from io import BytesIO

class jina:
    server_url = 'grpcs://dalle-flow.dev.jina.ai'
    def mega(prompt, n):
        if(len(prompt) == 0):
            prompt = 'an oil painting of a humanoid robot playing chess in the style of Matisse'

        doc = Document(text=prompt).post(jina.server_url, parameters={'num_images': n})
        da = doc.matches
        return da, doc
    
    def glide(fav, n):
        diffused = fav.post(f'{jina.server_url}', parameters={'skip_rate': 0.6, 'num_images': n}, target_executor='diffusion').matches
        return diffused
    
    def swinir(fav):
        fav = fav.post(f'{jina.server_url}/upscale')
        return fav

    def generate_images(query, number_of_images=2):
        da, doc = jina.mega(query, number_of_images)
        return da

    def generate_variations(url, number_of_images=4):
        return [i.blob for i in jina.glide(Document(url=url), n=number_of_images)]

    def upscale(url):
        return jina.swinir(Document(url=url))



if __name__ == "__main__":
    print("Initializing.......")
    print("We the best")
    prompt = str(input("Prompt: "))

    n = int(input("Number of Example Images: "))
    da, doc = jina.mega(prompt, n)
    da.plot_image_sprites(fig_size=(10,10), show_index=True)
    fav_id = int(input("Favourite ID.... "))

    fav = da[fav_id]
    fav.embedding = doc.embedding

    n = int(input("Number of Example Images: "))
    diffused = jina.glide(fav, n)
    diffused.plot_image_sprites(fig_size=(10,10), show_index=True)

    dfav_id = int(input("Favourite ID.... "))

    fav = diffused[dfav_id]
    fav = jina.swinir(fav)
    fav.display()

        
