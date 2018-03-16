def learn(sparse_matrix, labels, classifieur_constructor):
    classifieur = classifieur_constructor()
    classifieur.fit(sparse_matrix, labels)
    return classifieur


if __name__ == '__main__':
    pass
