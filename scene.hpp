#ifndef SCENE_H
#define SCENE_H

#include <vector>
#include "light.hpp"

class Scene
{
public:
    Scene(const Vector &ambientColor, const std::vector<Light> &lights);

    // Função para obter a cor ambiente
    Vector getAmbientColor() const;

    // Função para obter a lista de luzes
    const std::vector<Light> &getLights() const;

private:
    std::vector<Light> lights;
    Vector ambientColor;
};

#endif