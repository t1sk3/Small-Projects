const flock = [];

let alignSlider, cohesionSlider, seperationSlider;

function setup() {
    createCanvas(960, 540)
    alignSlider = createSlider(0, 5, 1, 0.1);
    cohesionSlider = createSlider(0, 5, 1, 0.1);
    seperationSlider = createSlider(0, 5, 1, 0.1);
    for (let i = 0; i < 100; i++) {
        flock.push(new Boid());
    }
}

function draw() {
    background(51);

    for (let boid of flock) {
        boid.edges();
        boid.flock(flock);
        boid.update();
        boid.show();
    }
}