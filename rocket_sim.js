// Scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);

// Camera
const camera = new THREE.PerspectiveCamera(
75,
window.innerWidth/window.innerHeight,
0.1,
1000
);

camera.position.set(0,3,10);

// Renderer
const renderer = new THREE.WebGLRenderer({antialias:true});
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);

// Lighting
const light = new THREE.DirectionalLight(0xffffff,1.5);
light.position.set(5,10,7);
scene.add(light);

const ambient = new THREE.AmbientLight(0x404040);
scene.add(ambient);

// Rocket
const geometry = new THREE.CylinderGeometry(0.5,0.5,5,32);
const material = new THREE.MeshStandardMaterial({color:0xffffff});

const rocket = new THREE.Mesh(geometry,material);

rocket.position.y = 2;

scene.add(rocket);

// Fire
const fireGeometry = new THREE.ConeGeometry(0.4,1.5,32);
const fireMaterial = new THREE.MeshBasicMaterial({color:0xff4500});

const fire = new THREE.Mesh(fireGeometry,fireMaterial);

fire.position.y = -3;

rocket.add(fire);

// Smoke particles
const smokeParticles = [];

for(let i=0;i<50;i++){

 const smokeGeometry = new THREE.SphereGeometry(0.2,8,8);
 const smokeMaterial = new THREE.MeshBasicMaterial({
   color:0x888888,
   transparent:true,
   opacity:0.6
 });

 const particle = new THREE.Mesh(smokeGeometry,smokeMaterial);

 particle.position.set(
   (Math.random()-0.5)*2,
   -3,
   (Math.random()-0.5)*2
 );

 scene.add(particle);

 smokeParticles.push(particle);

}

// Launch physics
let velocity = 0;

function animate(){

 requestAnimationFrame(animate);

 velocity += 0.002;

 rocket.position.y += velocity;

 smokeParticles.forEach(p=>{

   p.position.y -= 0.05;
   p.material.opacity -= 0.01;

   if(p.material.opacity < 0){
       p.material.opacity = 0.6;
       p.position.y = -3;
   }

 });

 renderer.render(scene,camera);

}

animate();
