import streamlit as st


def app():
    header = """
    <div align="center">
        <h1>Quantum App</h1>
    </div>
    <br /><br />
    """
    st.markdown(header, unsafe_allow_html=True)

    intro = """
    ## Why dockeurize your application ?
    Docker permit to create very light virtual environment and so to deploy any app on any system who support Docker (Linux, Mac, Windows, any Unix system, and more...).
    """
    st.markdown(intro)

    ####################################################################################
    # Dockerfile
    st.write("## Dockerfile")

    img_docker = """
    Except the `FROM` and the `CMD` instructions, you don't need to follow any order in the Dockerfile. Here it's my own writing reflexes.

    First, you need to precise which source image you want to use, usually it's an OS image but you can add layers of images.
    Here I create some intermediate images based on `Ubuntu` allow to use some quantum environment. 
    In this example I'm using my `Qiskit` image but more are available in the [DockerHub](https://hub.docker.com/search?q=mickahell%2Fquantum&type=image).
    ```
    FROM mickahell/quantum_lab_qiskit:latest
    """
    st.markdown(img_docker)

    var_docker = """
    Then the variables to use in your label or the var you need to steing up your different app version.
    ```
    ARG GITHUB_ACTOR
    ARG GITHUB_REPOSITORY
    ARG GITHUB_REF

    ARG DEBIAN_FRONTEND=noninteractive
    ARG LAB_ENV
    ENV LAB=${LAB_ENV}
    ENV TZ=Europe/Paris
    """
    st.markdown(var_docker)

    label_docker = """
    The labels are the metadata of your images and are useful to organize images, record information, ...
    It has different format of labels, here i'm using the [OCI IMAGE SPEC](https://github.com/opencontainers/image-spec).
    ```
    LABEL org.opencontainers.image.title="My super quantum app" \  
          org.opencontainers.image.authors=${GITHUB_ACTOR} \  
          org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \  
          org.opencontainers.image.source="https://quantum-lab.xtraorbitals.xyz" \  
          org.opencontainers.image.url="https://quantum-lab.xtraorbitals.xyz" \  
          org.opencontainers.image.description="Use the quantum mystery to explain life" \  
          org.opencontainers.image.os="Ubuntu Bionic" \  
          org.opencontainers.image.version=${GITHUB_REF}
    """
    st.markdown(label_docker)

    libs_docker = """
    Now the specific libs your program need, and add your source code to the container.
    ```
    RUN apt-get update -yq \  
    && apt-get install git -y
    RUN pip3 install autograd torch torchvision 
    
    ADD repo_of_my_app/ /opt/repo_app/
    ADD start.sh .
    """
    st.markdown(libs_docker)

    optional_docker = """
    <b>Optionally</b> you could need to open network ports, indicate a workdir or add volume to share data between your app and your host.
    ```
    EXPOSE 8080
    WORKDIR /opt/repo_app
    VOLUME /opt/repo_app/share
    """
    st.markdown(optional_docker, unsafe_allow_html=True)

    cmd_docker = """
    And finally add your command to start your program or a simple bash script who incoporate what your programm need to start.
    ```
    CMD /.start.sh
    """
    st.markdown(cmd_docker)

    ####################################################################################
    # Build & Run

    build_run = """
    ## Build & Run
    As soon as you finish your Dockerfile you now may want to build your image and to deploy it everywhere.
    """
    st.write(build_run)

    build_docker = """
    #### Build
    `docker build --tag my_quantum_app .`
    - You can precise custom var by using `--build-arg LAB_ENV=Qiskit` in your build.
    """
    st.markdown(build_docker)

    run_docker = """
    #### Run
    `docker run -d --name my_quantum_app my_quantum_app:latest`  
    - You can add different options :
        - to pair port `-p host_port:8080` 
        - to pair volume `-v host_repo:/opt/repo_app/share`
        - ...
    
    The whole documentation is available on the [Docker doc website](https://docs.docker.com/).
    """
    st.markdown(run_docker)

    conclude_docker = """
    Now your quantum application is running well anywhere you want. The platform you currently are, 
    is currently running using this kind of `Dockerfile` with `Quantum Lab Docker` layer. 
    Also The whole `Jupyter` are built using this `Dockerfile` with the affiliate `Quantum Lab` images as layer.  
    The whole code are available in [GitHub](https://github.com/mickahell/websites/tree/main/quantum_lab) and can be use as examples.
    """
    st.markdown(conclude_docker)
